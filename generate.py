from avatar_generator import AvatarGenerator


def generate_avatar():
    generator = AvatarGenerator("complexNFT\images")
    generator.generate_avatar(101)


if __name__ == "__main__":
    generate_avatar()