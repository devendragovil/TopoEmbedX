
# 🌐 TopoEmbedX: Representation Learning on Topological Domains 🍩


`TopoEmbedX` is a package for studying higher order representation learning on simplicial, cellular and combinatorial complexes.



## 🛠️ Main Features in Version 1.0

Support of higher order representation learning algorithms such as:
- DeepCell, 
- Cell2Vec, 
- Higher Order Laplacian Eigenmaps, and
- Higher Order Geometric Laplacian Eigenmaps

for the topological domains supported in [TopoNetX](https://github.com/pyt-team/TopoNetX).


## 🤖 Installing TopoEmbedX

1. Clone a copy of `TopoEmbedX` from source:
```bash
git clone https://github.com/pyt-team/TopoEmbedX
cd topoembedc
```
2. If you have already cloned `TopoEmbedX` from source, update it:
```bash
git pull
```
3. Install `TopoEmbedX` in editable mode:
```bash
pip install -e ".[dev,full]"
```
4. Install pre-commit hooks:
```bash
pre-commit install
```



## 🦾 Getting Started

```ruby
import topoembedx as tex
import toponetx as tnx

# create a cell complex object with a few cells
cx = tnx.CellComplex([[1, 2, 3, 4], [3,4,5,6,7,8]],ranks=2)

# create a model

model = tex.Cell2Vec()

# fit the model

model.fit(cx,neighborhood_type="adj", neighborhood_dim={"r": 1, "k": -1})
# here neighborhood_dim={"r": 1, "k": -1} specifies the dimension for
# which the cell embeddings are going to be computed.
# r=1 means that the embeddings will be computed for the first dimension.
# The integer 'k' is ignored and only considered
# when the input complex is a combinatorial complex.


# get the embeddings:

embeddings = model.get_embedding()

```

## 🔍 References ##

To learn more about topological representation learning.

- Mustafa Hajij, Ghada Zamzmi, Theodore Papamarkou, Nina Miolane, Aldo Guzmán-Sáenz, Karthikeyan Natesan Ramamurthy, Tolga Birdal, Tamal K. Dey, Soham Mukherjee, Shreyas N. Samaga, Neal Livesay, Robin Walters, Paul Rosen, Michael T. Schaub. [Topological Deep Learning: Going Beyond Graph Data](https://arxiv.org/abs/2206.00606).
```
@misc{hajij2023topological,
      title={Topological Deep Learning: Going Beyond Graph Data}, 
      author={Mustafa Hajij and Ghada Zamzmi and Theodore Papamarkou and Nina Miolane and Aldo Guzmán-Sáenz and Karthikeyan Natesan Ramamurthy and Tolga Birdal and Tamal K. Dey and Soham Mukherjee and Shreyas N. Samaga and Neal Livesay and Robin Walters and Paul Rosen and Michael T. Schaub},
      year={2023},
      eprint={2206.00606},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
