# tests.test_cluster.test_silhouette
# Tests for the SilhouetteVisualizer
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Mon Mar 27 10:01:37 2017 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: test_silhouette.py [57b563b] benjamin@bengfort.com $

"""
Tests for the SilhouetteVisualizer
"""

##########################################################################
## Imports
##########################################################################

from ..base import VisualTestCase

from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs

from yellowbrick.exceptions import YellowbrickValueError
from yellowbrick.cluster.silhouette import SilhouetteVisualizer


##########################################################################
## SilhouetteVisualizer Test Cases
##########################################################################

class SilhouetteVisualizerTests(VisualTestCase):

    def test_integrated_kmeans_silhouette(self):
        """
        Test no exceptions for kmeans silhouette visualizer on blobs dataset

        See #182: cannot use occupancy dataset because of memory usage
        """

        # Generate a blobs data set
        X, y = make_blobs(
            n_samples=1000, n_features=12, centers=8, shuffle=False, random_state=0
        )

        try:
            visualizer = SilhouetteVisualizer(KMeans(random_state=0))
            visualizer.fit(X)
            visualizer.poof()
            self.assert_images_similar(visualizer)
        except Exception as e:
            self.fail("error during silhouette: {}".format(e))

    def test_integrated_mini_batch_kmeans_silhouette(self):
        """
        Test no exceptions for mini-batch kmeans silhouette visualizer

        See #182: cannot use occupancy dataset because of memory usage
        """

        # Generate a blobs data set
        X, y = make_blobs(
            n_samples=1000, n_features=12, centers=8, shuffle=False, random_state=0
        )

        try:
            visualizer = SilhouetteVisualizer(MiniBatchKMeans(random_state=0))
            visualizer.fit(X)
            visualizer.poof()
            self.assert_images_similar(visualizer)
        except Exception as e:
            self.fail("error during silhouette: {}".format(e))
