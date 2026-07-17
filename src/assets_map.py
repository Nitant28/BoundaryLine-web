# -*- coding: utf-8 -*-
"""Local + downloaded asset paths for Boundaryline."""

LOCAL = {
    "hero_bat": "assets/alessandro-bogliari-oDs_AxeR5g4-unsplash.jpg",
    "hero_stadium": "assets/daniel-damasio-8t6WEecHe3U-unsplash.jpg",
    "hero_action": "assets/fotos-j5W9NJEkTF0-unsplash.jpg",
    "hero_field": "assets/moonwalkr-tquONxAKYXE-unsplash.jpg",
    "hero_player": "assets/yogendra-singh-dE3exzmYlKc-unsplash.jpg",
    "vision_match": "assets/vision-match.jpg",
    "logo": "assets/logo.png",
    "logo_dark": "assets/logo-dark.png",
}

DL = {
    "bat": "assets/cricket-bat.jpg",
    "action": "assets/cricket-action.jpg",
    "stadium": "assets/stadium-night.jpg",
    "lights": "assets/stadium-lights.jpg",
    "crowd": "assets/crowd-cheer.jpg",
    "fans": "assets/crowd-fans.jpg",
    "pitch": "assets/pitch.jpg",
    "trophy": "assets/trophy.jpg",
    "dusk": "assets/field-dusk.jpg",
    "ball": "assets/ball-close.jpg",
    "batsman": "assets/batsman.jpg",
    "celebration": "assets/celebration.jpg",
    "bowled": "assets/bowled.jpg",
}

# Prefer local downloads; fall back to hero locals if missing
def _safe(key, fallback):
    return DL.get(key) or fallback

HERO_LOCAL = [
    LOCAL["hero_bat"],
    LOCAL["hero_stadium"],
    LOCAL["hero_action"],
    LOCAL["hero_field"],
    LOCAL["hero_player"],
    DL["bat"],
    DL["action"],
    DL["stadium"],
    DL["lights"],
    DL["crowd"],
    DL["fans"],
    DL["pitch"],
    DL["trophy"],
    DL["dusk"],
    DL["ball"],
    LOCAL["hero_bat"],
    LOCAL["hero_action"],
    LOCAL["hero_stadium"],
    DL["crowd"],
    DL["lights"],
    LOCAL["hero_player"],
    DL["action"],
    DL["trophy"],
]
