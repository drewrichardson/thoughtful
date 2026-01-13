def main():
    sort(1,2,3,4)


def sort(w: int, h: int, l: int, m: int) -> str:
    """
    Categorizes a package based on its dimensions and mass.
    
    Args: 
        w: Width (cm), h: Height (cm), l: Length (cm), m: Mass (kg)
    Returns: 
        str: 'STANDARD', 'SPECIAL', or 'REJECTED'
    """
    MAX_DIM = 150
    VOL_LIMIT = 1_000_000
    
    is_bulky = (w * h * l >= VOL_LIMIT) or any(d >= MAX_DIM for d in (w, h, l))
    is_heavy = m >= 20
    
    if is_bulky and is_heavy:
        return 'REJECTED'
    if is_bulky or is_heavy:
        return 'SPECIAL'
    return 'STANDARD'


if __name__ == "__main__":
    main()
