
# Presentation collections

---

## What is this?

This is a collection of all my presentations written in markdown, and they are rendered in [remark.js](https://remarkjs.com) and [MathJax](https://www.mathjax.org).

The renderer is customized so that we can view all the presentations directly, and each presentation can has its own directory.

This collection can be used in a local server, like `http://127.0.0.1:9090/render/index.html?file=flask/microservices-flask-docker`, after starting a local server in root directory as

```python
python3 -m http.server 9090
```

Or we can use it in github pages in a similar way.

The query string `file=flask/microservices-flask-docker` assumes that

  * the root directory is the root directory of the collection
  * there is a `README.md` in directory `flask/microservices-flask-docker`

We can also use `file=flask/microservices-flask-docker/README.md` directly.

---

## Cross reference

For cross reference between presentation, we can use syntax 

```markdown
[title](render:/absolute/README.md)
```
or
```markdown
[title](render:./relative/README.md)
```

---

## Presentation list

  * [Microservices with flask](render://flask/microservices-flask-docker)

