from main import sort


class TestSort:
    """Test cases for package categorization function."""
    
    def test_standard_packages(self):
        """Test packages that are neither bulky nor heavy."""
        assert sort(10, 10, 10, 5) == "STANDARD"
        assert sort(50, 50, 50, 10) == "STANDARD"
        assert sort(149, 149, 7, 19) == "STANDARD"
    
    def test_bulky_by_volume(self):
        """Test packages that are bulky due to volume >= 1,000,000 cm³."""
        assert sort(100, 100, 100, 5) == "SPECIAL" 
        assert sort(101, 100, 100, 10) == "SPECIAL"  
    
    def test_bulky_by_dimension(self):
        """Test packages that are bulky due to any dimension >= 150 cm."""
        assert sort(150, 10, 10, 5) == "SPECIAL"
        assert sort(10, 150, 10, 5) == "SPECIAL"
        assert sort(10, 10, 150, 5) == "SPECIAL"
        assert sort(200, 50, 50, 10) == "SPECIAL"
    
    def test_heavy_packages(self):
        """Test packages that are heavy (>= 20 kg)."""
        assert sort(10, 10, 10, 20) == "SPECIAL"
        assert sort(50, 50, 50, 25) == "SPECIAL"
    
    def test_rejected_packages(self):
        """Test packages that are both bulky and heavy."""
        assert sort(150, 10, 10, 20) == "REJECTED"  # Bulky by dimension + heavy
        assert sort(100, 100, 100, 25) == "REJECTED"  # Bulky by volume + heavy
        assert sort(200, 200, 200, 30) == "REJECTED"  # Both bulky conditions + heavy
    
    def test_edge_cases(self):
        """Test boundary conditions."""
        assert sort(149, 149, 149, 19) == "SPECIAL" # Under, by volume over 1mil
        assert sort(99, 99, 99, 19) == "STANDARD"  # 970,299 cm
        
        assert sort(150, 1, 1, 1) == "SPECIAL"  # Exactly 150cm dimension
        assert sort(1, 1, 1, 20) == "SPECIAL"  # Exactly 20kg
        assert sort(100, 100, 100, 1) == "SPECIAL"  # Exactly 1,000,000 cm
        
        assert sort(1, 1, 1, 1) == "STANDARD"