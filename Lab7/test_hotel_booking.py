import pytest
from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label


@given(
    check_in=st.integers(min_value=1, max_value=28),
    nights=st.integers(min_value=1, max_value=30)
)
def test_nights_stayed_valid(check_in, nights):
    check_out = check_in + nights
    assert nights_stayed(f"{check_in}-{check_out}") == nights


@given(floor=st.integers(min_value=1, max_value=9),
       room=st.integers(min_value=0, max_value=99))
def test_room_floor_valid(floor, room):
    assert room_floor(f"D-{floor}{room:02d}") == floor


@given(names=st.lists(
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
    min_size=1, max_size=10
))
def test_booking_label_valid(names):
    result = booking_label(", ".join(names))
    expected = names[0].capitalize() + " +" + str(len(names) - 1)
    assert result == expected


@pytest.mark.parametrize("value", ["", "12", "12-abc", "1-2-3"])
def test_invalid_nights_input(value):
    with pytest.raises(ValueError):
        nights_stayed(value)


@pytest.mark.parametrize("value", ["", "D", "D-", "D-ABC"])
def test_invalid_room_code(value):
    with pytest.raises(ValueError):
        room_floor(value)


@pytest.mark.parametrize("value", ["", ",", "   "])
def test_invalid_guest_names(value):
    with pytest.raises(ValueError):
        booking_label(value)
