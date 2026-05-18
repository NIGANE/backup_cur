<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Deep Learning Keywords</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@400;700;800&display=swap');

  :root {
    --bg: #0b0e13;
    --surface: #13181f;
    --border: #1e2730;
    --accent: #4f8ef7;
    --accent2: #a78bfa;
    --accent3: #34d399;
    --accent4: #fb923c;
    --text: #e2e8f0;
    --muted: #64748b;
    --code-bg: #0d1117;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    min-height: 100vh;
    padding: 48px 24px;
  }

  .page {
    max-width: 860px;
    margin: 0 auto;
  }

  header {
    margin-bottom: 48px;
    border-left: 3px solid var(--accent);
    padding-left: 20px;
  }

  header h1 {
    font-size: 2.4rem;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.1;
  }

  header h1 span { color: var(--accent); }

  header p {
    color: var(--muted);
    margin-top: 8px;
    font-size: 0.95rem;
    font-family: 'JetBrains Mono', monospace;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    position: relative;
    overflow: hidden;
  }

  .card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
  }

  .card.blue::before  { background: var(--accent); }
  .card.purple::before { background: var(--accent2); }
  .card.green::before { background: var(--accent3); }
  .card.orange::before { background: var(--accent4); }

  .card-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }
  .blue  .card-tag { color: var(--accent); }
  .purple .card-tag { color: var(--accent2); }
  .green .card-tag { color: var(--accent3); }
  .orange .card-tag { color: var(--accent4); }

  .card h2 {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
  }

  .card p {
    color: #94a3b8;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 14px;
  }

  code {
    display: block;
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #7dd3fc;
    line-height: 1.7;
    white-space: pre;
  }

  .pill {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    padding: 3px 10px;
    border-radius: 20px;
    margin-top: 10px;
  }
  .blue  .pill { background: #1e3a5f; color: var(--accent); }
  .purple .pill { background: #2e1f5e; color: var(--accent2); }
  .green .pill { background: #064e3b; color: var(--accent3); }
  .orange .pill { background: #431407; color: var(--accent4); }

  .full {
    grid-column: 1 / -1;
  }

  .relation-box {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    line-height: 2;
    color: #94a3b8;
    margin-top: 10px;
  }

  .relation-box .highlight { color: var(--accent3); font-weight: 600; }
  .relation-box .dim { color: #475569; }

  footer {
    margin-top: 40px;
    text-align: center;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
  }

  @media (max-width: 600px) {
    .grid { grid-template-columns: 1fr; }
    .full { grid-column: 1; }
    header h1 { font-size: 1.8rem; }
  }
</style>
</head>
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
