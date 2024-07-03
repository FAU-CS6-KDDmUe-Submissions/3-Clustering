import random

from typing import List

from classes.cluster import Cluster
from classes.point import Point


class DBSCAN:
    """A DBSCAN clustering instance."""

    def __init__(self, epsilon: float, min_pts: int) -> None:
        """
        Initialize the DBSCAN clustering instance.

        Parameters:
        epsilon (float): The maximum distance between two points to be considered neighbors.
        min_pts (int): The minimum number of points in a neighborhood.
        """
        # The maximum distance between two points to be considered neighbors
        self.epsilon: float = epsilon

        # The minimum number of points in a neighborhood
        self.min_pts: int = min_pts

        # The clusters (contrary to KMeans, we do not know the number of clusters in advance)
        self.clusters: List[Cluster] = []

        # A list of points that are identified as noise
        self.noise: List[Point] = []

    def fit(self, points: List[Point]) -> None:
        """
        Fit the DBSCAN clustering instance to the given points.

        Parameters:
        points (List[Point]): The points to cluster.
        """
        # TODO
        raise NotImplementedError()

    def _get_neighborhood(self, point: Point, points: List[Point]) -> List[Point]:
        """
        Get the neighborhood of a point.

        Parameters:
        point (Point): The point to get the neighborhood of.
        points (List[Point]): The points to consider.

        Returns:
        List[Point]: The points in the neighborhood.
        """
        # TODO
        raise NotImplementedError()
