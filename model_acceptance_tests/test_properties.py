"""Property-based tests using Hypothesis.

For any valid input, the API should:
- Return HTTP 200
- Return a positive estimated value
"""

import httpx
from hypothesis import given, settings
from hypothesis import strategies as st

API_URL = "http://localhost:8000"

VALID_TYPES = [
    "Appartement",
    "Maison",
    "Dépendance",
    "Local industriel. commercial ou assimilé",
]

@settings(max_examples=20, deadline=None) #deadline set to None to avoid the error by slow response
@given(
    surface=st.floats(min_value=5.0, max_value=500.0),
    pieces=st.integers(min_value=1, max_value=20),
    departement=st.sampled_from(["75", "69", "13", "33", "92"]),
    type_local=st.sampled_from(VALID_TYPES),
)
def test_any_valid_input_returns_positive_estimate(surface, pieces, departement, type_local):
    """For any valid input, API must return 200 and a positive estimate."""
    response = httpx.post(
        f"{API_URL}/estimate/",
        json={
            "surface_reelle_bati": surface,
            "nombre_pieces_principales": pieces,
            "code_departement": departement,
            "type_local": type_local,
        },
        timeout=10.0,
    )
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
    data = response.json()
    assert "estimated_value_eur" in data, "Response missing estimated_value_eur"
    assert data["estimated_value_eur"] > 0, f"Expected positive value, got {data['estimated_value_eur']}"
