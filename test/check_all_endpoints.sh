#!/usr/bin/env bash

HOST="host.docker.internal:8088"

echo "Version:"
curl http://${HOST}/example/version
echo
echo

echo "Hello:"
curl http://${HOST}/example/hello
echo
echo

echo "Hello World with valid body:"
curl -d @test/bodies/hello_world_in.xml http://${HOST}/example/dynamic/hello-world
echo
echo

echo "Hello World with invalid body:"
curl -d 'Fail' http://${HOST}/example/dynamic/hello-world
echo
echo

echo "Hello World with no body:"
curl http://${HOST}/example/dynamic/hello-world
echo