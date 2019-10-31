#!/bin/bash

edc feeds list | parallel edc feed {} s3urls | grep \.db\.gz
