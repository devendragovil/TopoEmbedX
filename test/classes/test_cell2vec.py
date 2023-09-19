"""Test Cell2Vec class."""

import unittest

import numpy as np
import toponetx as tnx

from topoembedx.classes.cell2vec import Cell2Vec


class TestCell2Vec(unittest.TestCase):
    """Test Cell2Vec class."""

    def test_fit_and_get_embedding(self):
        """Test get_embedding."""
        # Create a small complex
        cx = tnx.CellComplex([[1, 2, 3, 4], [3, 4, 5, 6, 7, 8]], ranks=2)

        # Create a Cell2Vec object
        dc = Cell2Vec(dimensions=5)

        # Fit the Cell2Vec object to the graph and get embedding for nodes (using adjacency matrix A0)
        dc.fit(cx, neighborhood_type="adj", neighborhood_dim={"adj": 0, "coadj": -1})

        # Check that the shape of the embedding is correct
        assert dc.get_embedding().shape == (len(cx.nodes), 5)

        # Check that the shape of the embedding dictionary is correct
        ind = dc.get_embedding(get_dict=True)
        assert (len(ind)) == len(cx.nodes)

        # Check that the embedding of the first node is not equal to the embedding of the second node
        assert not np.allclose(dc.get_embedding()[0], dc.get_embedding()[1])


if __name__ == "__main__":
    unittest.main()
