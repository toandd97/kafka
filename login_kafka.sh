#!/bin/bash

# Prompt for the password securely
read -sp "mobio@kafka1's password: " mobio123

# Use `sudo -i` to switch to the kafka user
sudo -i -u kafka <<EOF
  # Go to the Kafka directory (assuming user kafka owns it)
  cd /home/kafka

  # Execute commands in the Kafka user's shell
  bash

  # Additional commands (if any) can be added here
EOF