import logging
import xml.etree.ElementTree as ET
from sqlalchemy import select
from pytrainer.waypoint import Waypoint
from pytrainer.gui.dialogs import save_file_chooser_dialog


class SaveGpx:
    def __init__(self, ddbb):
        self.ddbb = ddbb

    def _read_waypoints(self):
        stmt = (
            select(Waypoint)
            .where(Waypoint.lat.isnot(None), Waypoint.lon.isnot(None))
            .order_by(Waypoint.name)
        )
        with self.ddbb.session_scope() as session:
            return session.execute(stmt).scalars().all()

    def run(self):
        filename = save_file_chooser_dialog(
            title='Export Waypoints as GPX', pattern='*.gpx'
        )
        if filename is None:
            return
        if not filename.endswith('.gpx'):
            filename += '.gpx'

        waypoints = self._read_waypoints()

        gpx = ET.Element('gpx', version='1.1', creator='pytrainer')
        gpx.set('xmlns', 'http://www.topografix.com/GPX/1/1')

        for waypoint in waypoints:
            wpt = ET.SubElement(
                gpx, 'wpt', lat=str(waypoint.lat), lon=str(waypoint.lon)
            )
            if waypoint.ele is not None:
                ET.SubElement(wpt, 'ele').text = str(waypoint.ele)
            if waypoint.name:
                ET.SubElement(wpt, 'name').text = waypoint.name
            if waypoint.sym:
                ET.SubElement(wpt, 'sym').text = waypoint.sym
            if waypoint.time:
                ET.SubElement(wpt, 'time').text = (
                    waypoint.time.isoformat() + 'T00:00:00Z'
                )

        tree = ET.ElementTree(gpx)
        ET.indent(tree, space='  ')
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        logging.info('Exported %d waypoints to %s', len(waypoints), filename)

