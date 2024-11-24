import json
import csv
import xml.etree.ElementTree as ET


class BookAdapter:
    def import_books(self, data, format_type):
        if format_type == "JSON":
            return self._import_from_json(data)
        elif format_type == "CSV":
            return self._import_from_csv(data)
        elif format_type == "XML":
            return self._import_from_xml(data)
        else:
            raise ValueError("Unsupported format type")

    def _import_from_json(self, data):
        return json.loads(data)

    def _import_from_csv(self, data):
        books = []
        reader = csv.DictReader(data.splitlines())
        for row in reader:
            books.append(dict(row))
        return books

    def _import_from_xml(self, data):
        books = []
        root = ET.fromstring(data)
        for book in root.findall("book"):
            books.append({child.tag: child.text for child in book})
        return books
