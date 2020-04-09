def alphabeta(node, depth, α, β, maximizingPlayer):
    if depth == 0 
        return value
    if maximizingPlayer :
        value = -1000
        for move in self.availableMoves(self.map):
            value = max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α = max(α, value)
            if α ≥ β :
                break 
        return value
    else
        value = 1000
        for each child of node do
            value = min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β = min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value