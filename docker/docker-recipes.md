
# Recipes for Docker

---

## How to find out why container exits?

  * Replace the entrypoint to `/bin/bash`, and then figure out what happend in the container

```bash
docker run --rm -it --entrypoint /bin/bash image-name-or-id -s
```

  * `--entrypoint` makes the container execute `/bin/bash`, which gets `-s` as CMD, overwriting anything in the image might otherwise insist on
  * `--rm` is to automatically delete the container after exited
  * This method assumes there is `/bin/bash` in container

---

## How to reduce the context size when building?

  * Use `.dockerignore` file, for example

```
node_modules*
.git
```

---

