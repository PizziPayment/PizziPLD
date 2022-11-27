{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs-channels/archive/b58ada326aa612ea1e2fb9a53d550999e94f1985.tar.gz") { }
}:
let
  packages = python-packages: with python-packages; [
    pyyaml
  ];
  python-packages = pkgs.python3.withPackages packages;
in
pkgs.mkShell rec {
  buildInputs = with pkgs; [
    pandoc
    python-packages
    tectonic
  ];
}
