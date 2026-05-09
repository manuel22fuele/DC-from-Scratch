import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import pandas as pd
import numpy as np


def load_dataset(file_path, drop_columns=None):
    """
    Carrega dataset de ficheiro (.csv ou .txt) e devolve X (numpy array)
    """

    # Detectar tipo pelo nome
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file_path.endswith(".txt"):
        try:
            # tenta separar por vírgula
            df = pd.read_csv(file_path)
        except:
            try:
                # tenta por tab
                df = pd.read_csv(file_path, sep="\t")
            except:
                # fallback: espaços múltiplos
                df = pd.read_csv(file_path, delim_whitespace=True)

    else:
        raise ValueError("Formato não suportado (usa .csv ou .txt)")

    # Remover colunas indesejadas
    if drop_columns:
        df = df.drop(columns=drop_columns)

    # Manter só colunas numéricas
    df = df.select_dtypes(include=[np.number])

    # Converter para numpy
    X = df.values

    # -----------------------------
    # NORMALIZAÇÃO (essencial)
    # -----------------------------
    from sklearn.preprocessing import StandardScaler
    X = StandardScaler().fit_transform(X)

    # -----------------------------
    # PCA se tiver mais de 2 dimensões
    # -----------------------------
    if X.shape[1] > 2:
        from sklearn.decomposition import PCA
        X = PCA(n_components=2).fit_transform(X)

    return X




# -----------------------------
# Função genérica para gerar plots e métricas
# -----------------------------
def run_kmeans_analysis(X, dataset_name, k_range=range(2,11)):

    resultados = []

    for k in k_range:
        km = KMeans(n_clusters=k, init='random', n_init=10, max_iter=300, tol=1e-4, random_state=0)
        labels = km.fit_predict(X)

        distortion = km.inertia_
        sil_avg = silhouette_score(X, labels)

        centroids = [f"{{{c[0]:.2f}; {c[1]:.2f}}}" for c in km.cluster_centers_]

        resultados.append({
            "k": k,
            "silhouette": round(sil_avg,5),
            "distortion": round(distortion,2),
            "centroids": " | ".join(centroids)
        })

        # -----------------------------
        # Plots das 5 figuras
        # -----------------------------
        fig, axs = plt.subplots(2,3, figsize=(18,12))
        axs = axs.flatten()

        # Plot 1: Dataset original
        axs[0].scatter(X[:,0], X[:,1], c='white', edgecolor='black', s=50)
        axs[0].set_title(f"{dataset_name} - Dataset")
        axs[0].grid(True)

        # Plot 2: Clusters K-Means
        colors = ['lightgreen', 'orange', 'lightblue', 'pink', 'purple', 'yellow', 'cyan', 'magenta', 'brown', 'gray']
        markers = ['s', 'o', 'v', '^', 'D', '*', 'P', 'X', 'H', '+']
        for i in range(k):
            axs[1].scatter(X[labels==i,0], X[labels==i,1],
                           s=50, c=colors[i%len(colors)], marker=markers[i%len(markers)],
                           edgecolor='black', label=f'Cluster {i+1}')
        axs[1].scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], c='red', marker='*', s=250, label='Centroids')
        axs[1].set_title(f"K-Means Clusters (k={k})")
        axs[1].legend()
        axs[1].grid(True)

        # Plot 3: Elbow Method
        distortions = []
        for ki in range(2,11):
            km_tmp = KMeans(n_clusters=ki, init='k-means++', n_init=10, max_iter=300, random_state=0)
            km_tmp.fit(X)
            distortions.append(km_tmp.inertia_)
        axs[2].plot(range(2,11), distortions, marker='o')
        axs[2].set_title("Elbow Method")
        axs[2].set_xlabel("Número de clusters")
        axs[2].set_ylabel("Distortion")
        axs[2].grid(True)

        # Plot 4: Silhouette
        sil_vals = silhouette_samples(X, labels)
        y_lower, y_upper = 0, 0
        yticks = []
        cluster_labels = np.unique(labels)
        n_clusters = cluster_labels.shape[0]
        for i, c in enumerate(cluster_labels):
            c_sil_vals = sil_vals[labels==c]
            c_sil_vals.sort()
            y_upper += len(c_sil_vals)
            color = cm.jet(float(i)/n_clusters)
            axs[3].barh(range(y_lower, y_upper), c_sil_vals, height=1.0, edgecolor='none', color=color)
            yticks.append((y_lower + y_upper)/2)
            y_lower += len(c_sil_vals)
        axs[3].axvline(np.mean(sil_vals), color='red', linestyle='--')
        axs[3].set_yticks(yticks)
        axs[3].set_yticklabels(cluster_labels+1)
        axs[3].set_xlabel("Silhouette coefficient")
        axs[3].set_ylabel("Cluster")
        axs[3].set_title("Silhouette Plot")

        # Plot 5: Média da Silhueta vs K
        silhouette_avgs = []
        for ki in range(2,11):
            km_tmp = KMeans(n_clusters=ki, init='k-means++', n_init=10, max_iter=300, random_state=0)
            labels_tmp = km_tmp.fit_predict(X)
            silhouette_avgs.append(silhouette_score(X, labels_tmp))
        axs[4].plot(range(2,11), silhouette_avgs, marker='o', color='orange')
        axs[4].set_title("Média da Silhueta")
        axs[4].set_xlabel("Número de clusters")
        axs[4].set_ylabel("Silhueta média")
        axs[4].grid(True)

        axs[5].axis('off')  # último subplot vazio
        plt.tight_layout()
        plt.show()

        # Mini print
        print(f"\n{k=}: silhouette={sil_avg:.5f}, distortion={distortion:.2f}, centroids={centroids}\n")

    # Tabela final
    df = pd.DataFrame(resultados)
    print(f"\n=== Tabela de resultados para {dataset_name} ===\n")
    print(df.to_string(index=False))


# -----------------------------
# Exemplo de uso
# -----------------------------
from sklearn.datasets import make_circles, make_blobs, make_moons



# Escolhe o dataset que queres analisar
X_circles, _ = make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=0)
X_blobs, _   = make_blobs(n_samples=300, n_features=2, centers=8, cluster_std=0.5, random_state=0)
X_moons, _   = make_moons(n_samples=500, noise=0.05, random_state=0)

# Podes chamar para cada dataset
run_kmeans_analysis(X_circles, "make_circles")
run_kmeans_analysis(X_blobs, "make_blobs")
run_kmeans_analysis(X_moons, "make_moons")

########################

datasets = [
    ("data/dataset1.txt", "Dataset 1"),
    ("data/dataset2.txt", "Dataset 2"),
    ("data/dataset3.txt", "Dataset 3"),
    ("data/dataset4.txt", "Dataset 4")
]

for path, name in datasets:
    X = load_dataset(path)
    run_kmeans_analysis(X, name)