"""Acceptance test cases: each case represents one request to the model and the expected response.

Add or edit cases below to test different inputs. Each case has:
  - name: short label (e.g. "Paris apartment 50m2 3 rooms")
  - input: the four fields the API expects (surface, rooms, department, type)
  - expected_value_eur: optional; if set, the API response must be close to this value
  - expected_status: optional; if set, the API must return this HTTP status (e.g. 422 for validation errors)
"""

from model_acceptance_tests.test_case_schema import TestCase, TestCaseInput

# Case 1: Paris apartment, 50 m², 3 rooms
case_paris_apartment = TestCase(
    name="Paris apartment 50m2 3 rooms",
    input=TestCaseInput(
        surface_reelle_bati=50.0,
        nombre_pieces_principales=3.0,
        code_departement="75",
        type_local="Appartement",
    ),
)

# Case 2: House in Rhône, 100 m², 5 rooms
case_house_rhone = TestCase(
    name="House 100m2 5 rooms",
    input=TestCaseInput(
        surface_reelle_bati=100.0,
        nombre_pieces_principales=5.0,
        code_departement="69",
        type_local="Maison",
    ),
)

# Case 3: Small studio in Marseille, 20 m², 1 room
case_studio_marseille = TestCase(
    name="Marseille studio 20m2 1 room",
    input=TestCaseInput(
        surface_reelle_bati=20.0,
        nombre_pieces_principales=1.0,
        code_departement="13",
        type_local="Appartement",
    ),
)

# Case 4: Large house in Bordeaux, 200 m², 8 rooms
case_large_house_bordeaux = TestCase(
    name="Bordeaux large house 200m2 8 rooms",
    input=TestCaseInput(
        surface_reelle_bati=200.0,
        nombre_pieces_principales=8.0,
        code_departement="33",
        type_local="Maison",
    ),
)

# Case 5: Dépendance in Lyon, 15 m², 1 room
case_dependance_lyon = TestCase(
    name="Lyon dependance 15m2",
    input=TestCaseInput(
        surface_reelle_bati=15.0,
        nombre_pieces_principales=1.0,
        code_departement="69",
        type_local="Dépendance",
    ),
)

# Case 6: Commercial property in Paris, 80 m², 3 rooms
case_commercial_paris = TestCase(
    name="Paris commercial 80m2",
    input=TestCaseInput(
        surface_reelle_bati=80.0,
        nombre_pieces_principales=3.0,
        code_departement="75",
        type_local="Local industriel. commercial ou assimilé",
    ),
)

# Case 7: Invalid type_local — expect 422
case_invalid_type = TestCase(
    name="Invalid type_local returns 422",
    input=TestCaseInput(
        surface_reelle_bati=50.0,
        nombre_pieces_principales=3.0,
        code_departement="75",
        type_local="InvalidType",
    ),
    expected_status=422,
)

ACCEPTANCE_TEST_CASES = [
    case_paris_apartment,
    case_house_rhone,
    case_studio_marseille,
    case_large_house_bordeaux,
    case_dependance_lyon,
    case_commercial_paris,
    case_invalid_type,
]
