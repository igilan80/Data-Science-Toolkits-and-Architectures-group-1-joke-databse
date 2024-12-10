#!/bin/bash
# Log in to Weights & Biases
wandb login 59264a6e7a78aac4cc3d5465806b3e9a92648620
# Execute the container's main command
exec "$@"

