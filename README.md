# Zero to Hero: learning AI engineering from scratch
Following Karpathy's Neural Networks: Zero to Hero and building real understanding.
Every notebook here is typed by hand, no AI assistance. Progress is tracked by the checkboxes below.

# AI Engineering Roadmap (v2)

**Goal:** Become a real AI engineer who understands models from scratch, not a vibe coder.
**Pace:** My own. No deadlines.
**Everything below is free.** Tags: `[video]` `[book]` `[docs]` `[course]`

## Rules
- AI autocomplete OFF while following any lecture
- Type every line myself, video paused
- Use AI only to explain something I'm stuck on, never to write the code
- If something is fuzzy after one pass, move on and come back later
- **Ship something small after every lecture or module:** a notebook pushed to one public repo, plus 3-5 lines of notes in my own words
- **Just-in-time learning:** only learn the prep a stage actually needs, right before it

## How the stages fit together
1. Prep (lean) → 2. Karpathy → 3. Bridge (pick what pulls me) → 4. Prove it → 5. Specialize

---

## Stage 1: Lean prep

Only what micrograd needs. Everything else is learned just in time later.

### Setup
- [ ] Install Python and Jupyter
- [ ] Turn off Copilot / AI autocomplete
- [ ] Create one repo for all lecture notebooks and notes (public, so shipping is a habit)

### Python refresh (AI off)
- [ ] Write a `Value` class that holds a number
  - [ ] `__init__`
  - [ ] `__repr__`
  - [ ] `__add__`
  - [ ] `__mul__`
  - [ ] `Value(2) * Value(3) + Value(1)` prints correctly
- [ ] Write a closure (counter function that remembers its state)
- [ ] Use a lambda as a sort key
- [ ] Rewrite 3-4 old `for` loops as list/dict comprehensions
- [ ] Rebuild one small old project from scratch without AI

**Resources**
- `[course]` CS50P, Harvard's free Python course. Skim the weeks on classes, functions and file I/O: https://cs50.harvard.edu/python/
- `[book]` Automate the Boring Stuff with Python, free to read online: https://automatetheboringstuff.com
- `[video]` Corey Schafer's Python OOP tutorials on YouTube (search "Corey Schafer Python OOP"), good for dunder methods and classes

### Math: 3Blue1Brown
- [ ] Essence of Calculus
  - [ ] Derivatives
  - [ ] Chain rule
  - [ ] Implicit differentiation
  - [ ] Skim the rest
- [ ] Neural Networks series (first 4 videos)
  - [ ] Gradient descent
  - [ ] Backpropagation
- [ ] 5-10 chain rule problems by hand, e.g. `f(g(h(x)))`
- [ ] Plot a function and its derivative on the same chart (Matplotlib)
- [ ] Essence of Linear Algebra (can run alongside Stage 2; needed by lecture 3)
  - [ ] Vectors and linear combinations
  - [ ] Matrix multiplication as transformations
  - [ ] Dot products
  - [ ] Skip abstract vector spaces for now

**Resources**
- `[video]` 3Blue1Brown: the three series are on his YouTube channel as playlists, and the website has written lessons for them too: https://www.3blue1brown.com
- `[video]` Khan Academy for extra practice problems when something doesn't click: https://www.khanacademy.org/math/calculus-1
- `[book]` Mathematics for Machine Learning, free PDF (use as a reference, don't read cover to cover): https://mml-book.github.io
- `[docs]` Official Matplotlib tutorials: https://matplotlib.org/stable/tutorials/

### Ready for micrograd when I can:
- [ ] Explain what a derivative means without a formula
- [ ] Apply the chain rule to a composed function by hand
- [ ] Write a small class with operator overloading from memory

---

## Stage 2: Karpathy's Neural Networks: Zero to Hero

**Main resource**
- `[video]` Full playlist (about 19 hours of video, far more to do properly): https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- Code and notebooks: https://github.com/karpathy/nn-zero-to-hero
- Stuck on a lecture? Search the video's comments and the GitHub issues, and look at other people's notebook write-ups (search "Karpathy Zero to Hero notes")

### 2.1 Foundations
- [ ] **1. micrograd**: autograd engine, backprop, chain rule
  - [ ] Rewatch once before moving on (everything builds on it)
  - [ ] Ship: notebook + notes

### 2.2 Just-in-time prep before makemore
- [ ] NumPy essentials (broadcasting is the one that matters most)
  - [ ] Create arrays, slicing, reshape
  - [ ] Broadcasting
  - [ ] `sum(axis=...)`
  - [ ] Replace one Python loop with a vectorized operation
- [ ] Probability, only what makemore needs
  - [ ] Distributions
  - [ ] Expected value
  - [ ] Likelihood
  - [ ] Softmax
  - [ ] Cross-entropy loss (why it punishes confident wrong answers)
- [ ] PyTorch basics
  - [ ] Tensors, shapes, and indexing
  - [ ] `requires_grad` and `.backward()` (compare to my micrograd)
  - [ ] `nn.Module` and a basic training loop

**Resources**
- `[docs]` Official NumPy beginner guide and tutorials: https://numpy.org/learn/
- `[video]` freeCodeCamp's NumPy course on YouTube (search "freeCodeCamp NumPy")
- `[video]` StatQuest with Josh Starmer on YouTube, best for softmax, cross-entropy and likelihood (search "StatQuest cross entropy", "StatQuest likelihood"): https://statquest.org
- `[video]` Khan Academy Statistics and Probability: https://www.khanacademy.org/math/statistics-probability
- `[docs]` PyTorch official tutorials, start with the beginner basics: https://pytorch.org/tutorials/

### 2.3 makemore
- [ ] **2. makemore, bigram**: counting, loss, sampling
- [ ] **3. makemore, MLP**: embeddings, train/dev/test splits
- [ ] **4. makemore, activations and BatchNorm**: gradient health, vanishing/exploding gradients
- [ ] **5. makemore, backprop ninja**: manual backprop through tensors
  - *Skim-OK:* this one is brutal and the least essential. Watch it for intuition, do the exercises later if I want
- [ ] **6. makemore, WaveNet**: deeper architectures, reading PyTorch docs
- [ ] Ship after each one: notebook + notes

### 2.4 Transformers
- [ ] **7. Let's build GPT**: self-attention, multi-head attention, transformer blocks
- [ ] **8. Tokenizer**: build BPE from scratch
- [ ] *Optional:* Let's reproduce GPT-2 (124M)

**Companions when a lecture feels too fast**
- `[book]` Michael Nielsen, Neural Networks and Deep Learning (free online, great on backprop): http://neuralnetworksanddeeplearning.com
- `[book]` The Illustrated Transformer by Jay Alammar, to see attention visually before or after lecture 7: https://jalammar.github.io/illustrated-transformer/
- `[video]` 3Blue1Brown's deep learning chapters on transformers and attention

### Blank notebook test
- [ ] Build an MLP in PyTorch with no reference, and train it until loss drops
- [ ] Build a self-attention module with no reference and pass dummy data through it

---

## Stage 3: Bridge to my interests

Karpathy covers language models only. This fills the gap.
**Don't do all of it.** Audio is the default track because of the voice changer. Vision, agents and diffusion are optional: pick one or two that still pull me.

### Audio (default track, my live project: voice changer)
- [ ] DSP basics
  - [ ] Sampling rate and bit depth
  - [ ] Buffer size and latency
  - [ ] Time domain vs frequency domain (FFT)
  - [ ] Spectrograms and mel-spectrograms
- [ ] Load a .wav into NumPy and compute a mel-spectrogram myself
- [ ] Capture mic audio in small chunks with `sounddevice` and measure latency
- [ ] Hugging Face Audio course
- [ ] **Stepping stone:** build a small model on spectrograms myself (classifier or autoencoder) before touching voice-conversion code
  - [ ] Train it, plot the loss, look at what it reconstructs or misclassifies
- [ ] Read the RVC or VITS code
  - [ ] Trace tensor shapes through every layer
  - [ ] Find where content and speaker information separate
  - [ ] Understand the vocoder step (HiFi-GAN)

**Resources**
- `[video]` Valerio Velardo, "Audio Signal Processing for Machine Learning" on his YouTube channel The Sound of AI (search the title). Covers sound waves, the Fourier transform, spectrograms and librosa
- `[course]` Hugging Face Audio Course: https://huggingface.co/learn/audio-course
- `[book]` Think DSP by Allen Downey, signal processing taught with Python. Check his site, Green Tea Press, for the free version: https://greenteapress.com
- `[docs]` librosa docs and tutorials: https://librosa.org/doc/latest/
- `[docs]` sounddevice docs, for real-time streaming: https://python-sounddevice.readthedocs.io

### Vision (optional)
- [ ] fast.ai Practical Deep Learning
  - [ ] CNNs
  - [ ] Practical training workflow

**Resources**
- `[course]` fast.ai Practical Deep Learning for Coders (free, no ads, video lessons plus notebooks): https://course.fast.ai
- `[book]` The fastbook, the free book that goes with the course (Jupyter notebooks on GitHub, search "fastai fastbook")
- `[video]` MIT 6.S191 Introduction to Deep Learning, free on YouTube, good broad overview: http://introtodeeplearning.com

### Agents and RAG (optional)
- [ ] Hugging Face Agents course
- [ ] Understand tool calling (JSON schemas passed to the model)
- [ ] Understand the ReAct loop
- [ ] Understand embeddings and vector search (RAG)

**Resources**
- `[course]` Hugging Face Agents Course: https://huggingface.co/learn/agents-course
- `[course]` Hugging Face LLM Course, for fine-tuning and using Transformers: https://huggingface.co/learn/llm-course
- All Hugging Face courses in one place (also has MCP and Deep RL courses): https://huggingface.co/learn

### Diffusion (optional, only if images/video still pull me)
- [ ] fast.ai Part 2
- [ ] Hugging Face Diffusion course
- [ ] Learn the probability behind it (ELBO, score matching) before reading raw diffusion papers

**Resources**
- `[course]` fast.ai Part 2, Deep Learning Foundations to Stable Diffusion: https://course.fast.ai
- `[course]` Hugging Face Diffusion Models Course: https://huggingface.co/learn/diffusion-course
- `[book]` Lilian Weng's blog Lil'Log, her "What are Diffusion Models?" post is the standard written explanation: https://lilianweng.github.io

---

## Stage 4: Prove it

- [ ] Build one small project of my own
  - [ ] Idea: character-level model on text I love
  - [ ] Idea: tiny audio classifier
  - [ ] Write a short README: what it does, what I learned, what broke
- [ ] Read one paper with a companion walkthrough
  - [ ] Attention Is All You Need
  - [ ] Companion: Lilian Weng's blog posts and The Illustrated Transformer
- [ ] Implement one idea from that paper in PyTorch

**Resources**
- `[book]` Dive into Deep Learning, free interactive textbook with runnable code (use it as a reference for anything the project needs): https://d2l.ai
- `[docs]` Papers are free on arXiv: https://arxiv.org

---

## Stage 5: Specialize

- [ ] Pick one domain: audio / vision / LLMs / agents
- [ ] Go deep with papers and code
- [ ] Return to the voice changer and rebuild the parts I now understand
- [ ] Bring cybersecurity back as AI security

### Later topics, grouped by domain (not covered by Karpathy)
- **LLMs:** fine-tuning (LoRA / QLoRA), RLHF / DPO, scaling laws, modern tricks (RoPE, GQA, FlashAttention), training at scale
- **Audio:** neural vocoders beyond HiFi-GAN, streaming / low-latency inference
- **Agents:** evaluation, tool-use reliability, prompt-injection and other AI security risks

**Resources**
- `[course]` Hugging Face LLM Course covers fine-tuning: https://huggingface.co/learn/llm-course
- `[book]` Lil'Log has posts on many of these: https://lilianweng.github.io

---

## Notes
- Cybersecurity (TryHackMe) is paused, not dropped
- Free security practice for later:
  - PortSwigger Web Security Academy: https://portswigger.net/web-security
  - OverTheWire: https://overthewire.org
  - PicoCTF: https://picoctf.org
- Stuck? Rewatch, then sleep on it, then ask AI to *explain* (not write)
- If a link ever breaks, search the resource name. Course sites move around
