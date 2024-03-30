import os
import argparse
from IPython.display import SVG, display
import typst


def render_helper(formula,
                  src_output_path,
                  img_output_path,
                  fmt="svg",
                  preview=True):
    with open(src_output_path, "w") as f:
        f.write(formula)
    svg_bytes = typst.compile(src_output_path, format=fmt)
    with open(img_output_path, "wb") as f:
        f.write(svg_bytes)
    if preview:
        if fmt == "svg":
            display(SVG(img_output_path))
        else:
            raise ValueError("Only SVG format is supported for preview.")


class FormulaRenderer:
    """A class to render a formula to SVG using the typst library.

    Args:
        margin_h (str, optional): Horizontal margin. Defaults to "20pt".
        margin_v (str, optional): Vertical margin. Defaults to "20pt".
        align (str, optional): Alignment of the formula. Defaults to "center + horizon".
        override_config (str, optional): Override config for the formula.
            Defaults to "".

    Example:
        ```python
        renderer = FormulaRenderer(margin_h="20pt",
                                      margin_v="20pt",
                                      align="center + horizon")
        renderer.render("x^2 + y^2 = 1",
                        img_output_path="output.svg",
                        preview=True)
        ```
    """

    def __init__(self,
                 margin_h: str = "20pt",
                 margin_v: str = "20pt",
                 align: str = "center + horizon",
                 override_config: str = ""):
        self.margin_h = margin_h
        self.margin_v = margin_v
        self.align = align
        self.override_config = override_config
        self.template = self._generate_template()

    def _generate_template(self) -> str:
        return (
            f"#let display(body) = context {{\n"
            f"  set page(width: auto, height: auto, margin: (x: {self.margin_h}, y: {self.margin_v}))\n"
            f"  {self.override_config}\n"
            f"  align([#body], {self.align})\n"
            f"}}\n")

    def render(self,
               formula,
               name=None,
               fmt="svg",
               src_output_path=None,
               img_output_path=None,
               preview=True):
        """Render the formula to SVG.

        Args:
            formula (str): The formula to render.
            name (str, optional): Name of the output file. Defaults to None.
                If name is provided, src_output_path and img_output_path are
                automatically set to "output/{name}.typ" and
                "output/{name}.svg" respectively.
            fmt (str, optional): Output format. Defaults to "svg".
            src_output_path (str, optional): Output path for the intermediate
                .typ file. Defaults to None.
            img_output_path (str, optional): Output path for the rendered SVG
                image. Defaults to None.
            preview (bool, optional): Whether to display the rendered image.
                Defaults to True.
        """
        if name is not None:
            os.makedirs("output", exist_ok=True)
            src_output_path = f"output/{name}.typ"
            img_output_path = f"output/{name}.svg"
        else:
            if img_output_path is not None:
                src_output_path = src_output_path or os.path.splitext(
                    img_output_path)[0] + ".typ"
            elif not preview:
                raise ValueError(
                    "img_output_path is required if not preview and name"
                    "is not provided.")
            else:
                src_output_path = "output.typ"
                img_output_path = "output.svg"
        src = self.template + f"\n#display[{formula}]"
        render_helper(src,
                      src_output_path,
                      img_output_path,
                      fmt=fmt,
                      preview=preview)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "formula",
        type=str,
        help=(
            "The formula to render. Use singe quotes to avoid shell expansion."
            "e.g. 'x^2 + y^2 = 1'"))
    parser.add_argument("--output_path",
                        "-o",
                        type=str,
                        default="output.svg",
                        help="Output path for the rendered SVG image.")
    parser.add_argument("--margin_h",
                        type=str,
                        default="20pt",
                        help="Horizontal margin.")
    parser.add_argument("--margin_v",
                        type=str,
                        default="20pt",
                        help="Vertical margin.")
    parser.add_argument("--align",
                        type=str,
                        default="center + horizon",
                        help="Alignment of the formula.")
    parser.add_argument("--override_config",
                        type=str,
                        default="",
                        help="Override config for the formula.")
    args = parser.parse_args()
    # Check file extension is .svg
    if os.path.splitext(args.output_path)[1] != ".svg":
        raise ValueError("Output file must be an SVG file.")
    print("Rendering the following formula to", args.output_path)
    print("\n\t", args.formula, "\n")
    renderer = FormulaRenderer(margin_h=args.margin_h,
                               margin_v=args.margin_v,
                               align=args.align,
                               override_config=args.override_config)
    renderer.render(args.formula,
                    img_output_path=args.output_path,
                    preview=False)
