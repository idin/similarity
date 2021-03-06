from jellyfish import jaro_winkler as _get_jaro_winkler_similarity


def get_jaro_winkler_similarity(s1, s2, case_sensitive=True):
	if not case_sensitive:
		s1 = s1.lower()
		s2 = s2.lower()
	return _get_jaro_winkler_similarity(s1, s2)


def get_jaro_winkler_distance(s1, s2, case_sensitive=True):
	return max(len(s1), len(s2))*(1-get_jaro_winkler_similarity(s1, s2, case_sensitive=case_sensitive))

