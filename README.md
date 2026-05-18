
<title>Deep Learning Keywords</title>

<body>
<div class="page">

  <header>
    <h1>Deep Learning<br><span>Keywords</span></h1>
    <p>// your personal cheat sheet</p>
  </header>

  <div class="grid">

    <!-- Tensor -->
    <div class="card blue">
      <div class="card-tag">core data</div>
      <h2>Tensor</h2>
      <p>A multi-dimensional array. The fundamental data structure for everything in deep learning — data, weights, outputs, all tensors.</p>
      <code>scalar  →  0D  →  42
vector  →  1D  →  [1, 2, 3]
matrix  →  2D  →  [[1,2],[3,4]]
tensor  →  3D+ →  image, video...</code>
      <span class="pill">= just a multi-dim array</span>
    </div>

    <!-- PyTorch -->
    <div class="card purple">
      <div class="card-tag">framework</div>
      <h2>PyTorch / Torch</h2>
      <p>Same thing. "Py" + "Torch" = Python version of the original Torch library. Always imported as <em>torch</em>.</p>
      <code>import torch   # ← always this

# NOT: import pytorch ❌</code>
      <span class="pill">torch = pytorch = same thing</span>
    </div>

    <!-- Weights -->
    <div class="card green">
      <div class="card-tag">what the network learns</div>
      <h2>Weights</h2>
      <p>Tensors (matrices of numbers) connecting neurons. Start random, get adjusted during training. This is what "learning" actually means.</p>
      <code>layer.weight
# tensor([[ 0.31, -0.18,  0.42],
#         [-0.23,  0.51, -0.08],
#         [ 0.12, -0.45,  0.33]])</code>
      <span class="pill">weights = tensors</span>
    </div>

    <!-- Neural Network -->
    <div class="card orange">
      <div class="card-tag">the concept</div>
      <h2>Neural Network</h2>
      <p>Graph of nodes (neurons) connected by lines (weights). Inspired by the brain. In reality: just tensors and matrix math.</p>
      <code>input → [layer1] → [layer2] → output
         ↑ tensors flow through layers ↑</code>
      <span class="pill">graph of nodes = tensor math</span>
    </div>

    <!-- Forward Pass -->
    <div class="card blue">
      <div class="card-tag">inference</div>
      <h2>Forward Pass</h2>
      <p>Data travels through all layers from input to output — in one direction only. Happens every time you use a model (training or inference).</p>
      <code>input → layer1 → layer2 → ... → output
         data moves forward, no going back</code>
      <span class="pill">happens always</span>
    </div>

    <!-- Backward Pass -->
    <div class="card purple">
      <div class="card-tag">training only</div>
      <h2>Backward Pass</h2>
      <p>After a forward pass, the error travels BACKWARDS through layers to figure out which weights caused the mistake. Only during training.</p>
      <code>loss.backward()   # PyTorch does this
optimizer.step()  # fixes the weights</code>
      <span class="pill">training only</span>
    </div>

    <!-- Loss -->
    <div class="card green">
      <div class="card-tag">error measurement</div>
      <h2>Loss</h2>
      <p>A number measuring how wrong the prediction was. The network's goal is to make this number as small as possible.</p>
      <code>prediction: 30% cat
reality:   100% cat
loss:      big number → weights need fixing</code>
      <span class="pill">smaller = better</span>
    </div>

    <!-- Epoch -->
    <div class="card orange">
      <div class="card-tag">training cycle</div>
      <h2>Epoch</h2>
      <p>One full cycle through ALL your training data. More epochs = more chances to learn. Not the same as "layers" — that's depth.</p>
      <code>1 epoch  = sees all 1000 images once
10 epochs = sees all 1000 images 10x</code>
      <span class="pill">≠ layers (different concept)</span>
    </div>

    <!-- Deep vs ML full width -->
    <div class="card blue full">
      <div class="card-tag">big picture</div>
      <h2>Machine Learning vs Deep Learning</h2>
      <p>Deep Learning is a subset of Machine Learning. The key difference is who extracts the features.</p>
      <div class="relation-box">
<span class="highlight">Machine Learning</span>  →  YOU extract features manually → algorithm learns
<span class="highlight">Deep Learning    </span>  →  YOU define structure + math  → network learns features by itself
<span class="dim">
All Deep Learning is Machine Learning.
Not all Machine Learning is Deep Learning.</span>
      </div>
    </div>

    <!-- What you define vs network -->
    <div class="card purple full">
      <div class="card-tag">responsibility split</div>
      <h2>You vs The Network</h2>
      <p>You are the architect. The network is the learner.</p>
      <div class="relation-box">
<span class="highlight">YOU define:</span>                    <span class="highlight">NETWORK learns:</span>
─────────────────────────────────────────────────────
how many layers                    the weights inside layers
what math happens (relu, etc.)     what patterns matter
how data flows between layers      which neurons activate
loss function + learning rate      nothing else — just weights
      </div>
    </div>

  </div>

  <footer>deep learning cheat sheet &nbsp;·&nbsp; built with Claude</footer>

</div>
</body>
</html>
