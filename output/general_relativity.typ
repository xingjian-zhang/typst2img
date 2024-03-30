#let display(body) = context {
  set page(width: auto, height: auto, margin: (x: 20pt, y: 20pt))
  
  align([#body], center + horizon)
}

#display[$ G_(mu nu) + Lambda g_(mu nu) = kappa T_(mu nu) $]