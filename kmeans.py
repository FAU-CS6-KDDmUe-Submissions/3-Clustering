import random

from typing import List

from classes.point import Point
from classes.cluster import Cluster


class KMeans:
    """
    A K-Means clustering instance.
    """

    def __init__(self, k: int):
        """
        Initialize the K-Means clustering instance.

        Parameters:
        k (int): The number of clusters to create
        """
        # The number of partitions/clusters to create
        self.k: int = k

        # Create the partitions/clusters
        self.partitions: List[Cluster] = [Cluster() for _ in range(k)]

        # The centroids of the partitions
        self.centroids: List[Point] = [None for _ in range(k)]

    def fit(self, points: List[Point]):
        """
        Fit the K-Means clustering instance to the given points.

        Parameters:
        points (List[Point]): The points to cluster
        """
        # TODO
        raise NotImplementedError()

    def _initialize_partitions(self, points: List[Point]):
        """
        Initializes the partitions (self.partitions) by assigning each point to a cluster/partition.
        All clusters/partitions are non empty after this method is called.

        Parameters:
        points (List[Point]): The points to cluster
        """
        # Check if the number of points is greater or equal to the number of clusters
        if len(points) < self.k:
            raise ValueError(
                "Number of points has to be greater or equal to the number of clusters."
            )

        # TODO
        raise NotImplementedError()

    def _update_centroids(self):
        """
        Updates the centroids of the partitions and writes the new centroids into self.centroids.
        """
        # Make sure that all partitions are non-empty
        for partition in self.partitions:
            if len(partition) == 0:
                # Throw an error if a partition is empty
                raise ValueError(
                    "All partitions have to be non-empty before updating the centroids."
                )

        # TODO
        raise NotImplementedError()

    def _reassign_points(self) -> bool:
        """
        Reassigns each point to the partition with the closest centroid.

        Ensures that each partition is non-empty after reassigning the points,
        by randomly reassigning a single point from a random non-empty partition
        with more than one element into each empty partition.

        This is necessary to avoid empty partitions, which would lead to k-means
        not producing k clusters, but k-n clusters (n is the number of empty partitions).

        Returns:
        bool: True if the reassignment changed the partitions, False otherwise
        """
        # TODO
        raise NotImplementedError()
