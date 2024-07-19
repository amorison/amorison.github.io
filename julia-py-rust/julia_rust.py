import numpy as np
from PIL import Image
from juliaset import ComplexRegion, JuliaDiv


def main() -> None:
    plane = ComplexRegion(xleft=-1e-1, xright=1e-1, yleft=1e-1, yright=-1e-1)
    julia_div = JuliaDiv(
        c_0=complex(-0.835, -0.2321),
        resolution=4000,
        n_iterations=(20, 100),
    )
    div_map = julia_div.over(plane)

    im = Image.fromarray((div_map * 255).astype(np.uint8).T)
    im.save("plot.png")


if __name__ == "__main__":
    main()
