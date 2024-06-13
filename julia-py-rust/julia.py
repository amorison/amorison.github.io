from dataclasses import dataclass

from numpy.typing import NDArray
import numpy as np
from PIL import Image


@dataclass
class ComplexRegion:
    xleft: float
    xright: float
    yleft: float
    yright: float

    def xspan(self) -> float:
        return abs(self.xright - self.xleft)

    def yspan(self) -> float:
        return abs(self.yright - self.yleft)

    def build(self, resolution_x: int) -> NDArray[np.complexfloating]:
        x_s = np.linspace(self.xleft, self.xright, resolution_x)
        y_s = np.linspace(self.yleft, self.yright,
                          int(resolution_x * self.yspan() / self.xspan()))
        return x_s[:, np.newaxis] + y_s[np.newaxis, :] * 1j


@dataclass
class JuliaDiv:
    c_0: complex
    threshold: float = 2.0
    n_iterations: tuple[int, int] = (0, 50)
    resolution: int = 1000

    def over(self, plane: ComplexRegion) -> NDArray[np.floating]:
        itermin, itermax = self.n_iterations
        assert itermin < itermax
        z_s = plane.build(self.resolution)
        div = np.full_like(z_s, itermax, dtype=np.uint32)
        for i in range(itermax):
            z_s = np.square(z_s) + self.c_0
            diverged = np.abs(z_s) >= self.threshold
            div[diverged] = np.uint32(i)
            z_s[diverged] = np.nan
        return (np.maximum(div, itermin) - itermin) / (itermax - itermin)


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
