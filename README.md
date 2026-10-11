# AI Engineering Roadmap (v3)

**Goal:** Become a real AI engineer who understands models from scratch, not a vibe coder.
**Core interests:** LLMs, computer vision, diffusion models. Open to new ones (agents, for example) as I learn.
**Pace:** My own. No deadlines.
**Everything below is free.** Tags: `[video]` `[book]` `[docs]` `[course]`

## Rules
- **No AI while learning.** AI is for building (side hustle) only
- AI autocomplete OFF in this repo
- Type every line myself, video paused
- If something is fuzzy after one pass, log it and move on, then come back later
- Ship something small after every lecture or module: a notebook in the public repo plus 3-5 lines of notes
- Just-in-time learning: only learn the prep a stage actually needs, right before it

---

## Where I am
**Now:** Stage 1, Setup
*(Update this line whenever I move. Only the current stage matters. Everything else on this page is a map, not a to-do list.)*

## The big picture

| Stage | What | Why |
|---|---|---|
| 1 | Lean prep | Just enough Python and calculus to start |
| 2 | Karpathy's Zero to Hero | The shared foundation for LLMs, vision and diffusion |
| 3 | Branches | LLMs, vision, diffusion, plus an explore slot for new interests |
| 4 | Prove it | One project and one paper, from scratch |
| 5 | Specialize | Go deep on one branch |

**Stages 1 and 2 are the same for every interest.** I don't have to choose anything until Stage 3.

---

## Stage 1: Lean prep

Only what micrograd needs. Everything else is learned just in time later.

### Setup
- [x] Install Python
- [x] Install VS Code with the Python and Jupyter extensions
- [x] Create the repo and the Obsidian vault (see the playbook)
- [x] Turn off Copilot and AI suggestions for this repo

### Python refresh (AI off)
- [x] Write a `Value` class that holds a number
  - [x] `__init__`
  - [x] `__repr__`
  - [x] `__add__`
  - [x] `__mul__`
  - [x] `Value(2) * Value(3) + Value(1)` prints correctly
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
- [ ] Essence of Linear Algebra (can run alongside Stage 2, needed by lecture 3)
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

The foundation for everything after it. No branching yet.

**Main resource**
- `[video]` Full playlist (about 19 hours of video, far more to do properly): https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- Code and notebooks: https://github.com/karpathy/nn-zero-to-hero
- Stuck on a lecture? Use the stuck protocol in the playbook. Look at the video's comments, the GitHub issues, and other people's notebook write-ups (search "Karpathy Zero to Hero notes")

### 2.1 Foundations
- [ ] **1. micrograd**: autograd engine, backprop, chain rule
  - [ ] Rewatch once before moving on (everything builds on it)
  - [ ] Ship: notebook + notes

### 2.2 Just-in-time prep before makemore
- [ ] NumPy essentials (broadcasting matters most)
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
  - [ ] Tensors, shapes, indexing
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
  - *Skim-OK:* brutal and the least essential. Watch it for intuition, do the exercises later if I want
- [ ] **6. makemore, WaveNet**: deeper architectures, reading PyTorch docs
- [ ] Ship after each one: notebook + notes

### 2.4 Transformers (my first from-scratch LLM)
- [ ] **7. Let's build GPT**: self-attention, multi-head attention, transformer blocks
- [ ] **8. Tokenizer**: build BPE from scratch
- [ ] *Optional:* Let's reproduce GPT-2 (124M)

**Companions when a lecture feels too fast**
- `[book]` Michael Nielsen, Neural Networks and Deep Learning (free online, great on backprop): http://neuralnetworksanddeeplearning.com
- `[book]` The Illustrated Transformer by Jay Alammar, to see attention visually before or after lecture 7: https://jalammar.github.io/illustrated-transformer/
- `[video]` 3Blue1Brown's deep learning chapters on transformers and attention
- `[docs]` PyTorch official tutorials, for reading docs like a pro: https://pytorch.org/tutorials/

### Blank notebook test
- [ ] Build an MLP in PyTorch with no reference, and train it until loss drops
- [ ] Build a self-attention module with no reference and pass dummy data through it

### Checkpoint before Stage 3
- [ ] I can explain backprop, embeddings and attention in my own words
- [ ] My repo has a notebook for every lecture I finished

---

## Stage 3: Branches

Karpathy covers language models only. This stage covers the rest of my interests.
**I do not need to do all of it at once.** Each branch stands alone. Pick one, finish its core items, then pick the next.

**Suggested order:** LLMs → Vision → Diffusion. Diffusion builds on vision, so keep those two in that order. Reorder freely, and use the explore slot for anything new.

### Branch A: LLMs (deepening)
- [ ] Hugging Face LLM Course: using Transformers, fine-tuning
- [ ] Fine-tune a small model on a small dataset (LoRA when I'm ready)
- [ ] Compare my from-scratch GPT to a pretrained one: what's different?

**Resources**
- `[course]` Hugging Face LLM Course: https://huggingface.co/learn/llm-course
- `[book]` Lilian Weng's blog Lil'Log has posts on many LLM topics: https://lilianweng.github.io

### Branch B: Computer vision
- [ ] fast.ai Practical Deep Learning (Part 1)
  - [ ] CNNs
  - [ ] Practical training workflow
- [ ] Train an image classifier on a dataset I care about
- [ ] Build a small CNN from scratch in PyTorch (no fastai helpers)

**Resources**
- `[course]` fast.ai Practical Deep Learning for Coders (free, no ads, video lessons plus notebooks): https://course.fast.ai
- `[book]` The fastbook, the free book that goes with the course (Jupyter notebooks on GitHub, search "fastai fastbook")
- `[video]` MIT 6.S191 Introduction to Deep Learning, free on YouTube, good broad overview: http://introtodeeplearning.com
- `[book]` Dive into Deep Learning, free interactive textbook with runnable code (use as reference): https://d2l.ai

### Branch C: Diffusion models (after Branch B)
- [ ] fast.ai Part 2 (Deep Learning Foundations to Stable Diffusion)
- [ ] Hugging Face Diffusion Models Course
- [ ] Learn the probability behind it (ELBO, score matching) before reading raw diffusion papers
- [ ] Train a tiny diffusion model on a small image dataset

**Resources**
- `[course]` fast.ai Part 2: https://course.fast.ai
- `[course]` Hugging Face Diffusion Models Course: https://huggingface.co/learn/diffusion-course
- `[book]` Lilian Weng's "What are Diffusion Models?" post, the standard written explanation: https://lilianweng.github.io

### Explore slot: new interests (agents, or anything else)
Agents and RAG are the first candidate. The same protocol works for any new interest.

**Try-it protocol (time-boxed)**
1. Do the first module or lesson of the course
2. Build one tiny thing with what I learned
3. Decide: **Add** it as a branch / **Park** it in the Parking Lot below / **Drop** it
4. Never explore more than one new interest at a time

**Agents and RAG, if I explore them**
- [ ] Hugging Face Agents course
- [ ] Understand tool calling (JSON schemas passed to the model)
- [ ] Understand the ReAct loop
- [ ] Understand embeddings and vector search (RAG)

**Resources**
- `[course]` Hugging Face Agents Course: https://huggingface.co/learn/agents-course
- All Hugging Face courses in one place (also has MCP and Deep RL courses): https://huggingface.co/learn

---

## Stage 4: Prove it

- [ ] Build one small project of my own, from my strongest branch
  - [ ] Idea: character-level model on text I love (LLMs)
  - [ ] Idea: small image classifier or tiny diffusion model on a small dataset (vision / diffusion)
  - [ ] Idea: a small agent with tool calling, if I added agents
  - [ ] Write a short README: what it does, what I learned, what broke
- [ ] Read one paper with a companion walkthrough
  - [ ] LLMs: Attention Is All You Need (companions: Lil'Log and The Illustrated Transformer)
  - [ ] Or a core paper from my branch (vision or diffusion)
- [ ] Implement one idea from that paper in PyTorch

**Resources**
- `[book]` Dive into Deep Learning, free interactive textbook with runnable code (use it as a reference for anything the project needs): https://d2l.ai
- `[docs]` Papers are free on arXiv: https://arxiv.org

---

## Stage 5: Specialize

- [ ] Pick one domain: LLMs / vision / diffusion / agents (or something new)
- [ ] Go deep with papers and code
- [ ] Bring cybersecurity back as AI security

### Later topics, grouped by domain
- **LLMs:** RLHF / DPO, scaling laws, modern tricks (RoPE, GQA, FlashAttention), training at scale
- **Vision:** deeper architectures, detection and segmentation, vision transformers
- **Diffusion:** latent diffusion, conditioning and guidance, newer sampling methods
- **Agents:** evaluation, reliability of tool use, prompt-injection and other AI security risks

---

## Parking Lot
Interests I've noticed but haven't started. Writing them here is enough for now.
- 

---

## Notes
- Cybersecurity (TryHackMe) is paused, not dropped
- Free security practice for later:
  - PortSwigger Web Security Academy: https://portswigger.net/web-security
  - OverTheWire: https://overthewire.org
  - PicoCTF: https://picoctf.org
- Stuck? Use the stuck protocol in the playbook (no AI)
- If a link ever breaks, search the resource name. Course sites move around