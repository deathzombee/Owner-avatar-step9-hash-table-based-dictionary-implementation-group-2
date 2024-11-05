import difflib


# Gabriel Calderon
class FuzzySearch:
    """works with both with objects in a list or dict"""

    def __init__(self, satellites):
        self.satellites = satellites

    def search(self, query, threshold=0.6):
        results = []
        for satellite in self.satellites:
            name_ratio = difflib.SequenceMatcher(
                None, query.lower(), satellite.name.lower()
            ).ratio()
            if name_ratio >= threshold:
                results.append((satellite, name_ratio))

        # Sort results by similarity ratio in descending order
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def search_by_attribute(self, query, attribute, threshold=0.6):
        results = []
        for satellite in self.satellites:
            attr_value = getattr(satellite, attribute, "")
            if attr_value is not None:
                attr_ratio = difflib.SequenceMatcher(
                    None, query.lower(), str(attr_value).lower()
                ).ratio()
                if attr_ratio >= threshold:
                    results.append((satellite, attr_ratio))

        # Sort results by similarity ratio in descending order
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def search_all_attributes(self, query, threshold=0.6):
        results = []
        attributes = [
            "name",
            "orbit_type",
            "orbit_height",
            "cycle",
            "date",
            "oos_date",
            "org",
        ]

        for satellite in self.satellites:
            max_ratio = 0
            for attr in attributes:
                attr_value = getattr(satellite, attr, "")
                if attr_value is not None:
                    ratio = difflib.SequenceMatcher(
                        None, query.lower(), str(attr_value).lower()
                    ).ratio()
                    max_ratio = max(max_ratio, ratio)

            if max_ratio >= threshold:
                results.append((satellite, max_ratio))

        # Sort results by similarity ratio in descending order
        results.sort(key=lambda x: x[1], reverse=True)
        return results
