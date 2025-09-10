"""
Clustering engine for ReliefOn: Groups similar disaster requests
"""

from sklearn.cluster import KMeans
import numpy as np

def cluster_requests(requests, num_clusters=5):
    """
    requests: list of dictionaries with 'lat' and 'lon' keys
    Returns a dictionary mapping cluster labels to requests
    """
    if not requests:
        return {}

    coords = np.array([[r['lat'], r['lon']] for r in requests])
    num_clusters = min(num_clusters, len(coords))
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(coords)
    labels = kmeans.labels_
    
    clustered = {}
    for idx, label in enumerate(labels):
        clustered.setdefault(label, []).append(requests[idx])
    
    return clustered

if __name__ == "__main__":
    sample_requests = [
        {"lat": 12.97, "lon": 77.59, "desc": "Need water"},
        {"lat": 12.98, "lon": 77.60, "desc": "Food required"},
        {"lat": 13.00, "lon": 77.58, "desc": "Medical assistance"}
    ]
    clusters = cluster_requests(sample_requests, num_clusters=2)
    print(clusters)
