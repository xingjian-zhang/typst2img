#let display(body) = context {
  let size = measure(body)
  set page(width: size.width + 20pt, height: size.height + 20pt)
  
  align([#body], center + horizon)
}

#display[$ G_(mu nu) + Lambda g_(mu nu) = kappa T_(mu nu) $]