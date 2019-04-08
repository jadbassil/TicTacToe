from Node import Node

def alpha_beta_rac(node, level):
    alpha = -9999
    beta = 9999
    if not node.successors:
        return node
    children = node.successors
    while children:
        score = alpha_beta(children[0], node.inverse_level(), alpha, beta)
        if score > alpha:
            alpha = score
            succ_node = children[0]
        children.pop(0)
    return succ_node if succ_node else None

def alpha_beta(node, level, alpha, beta):
    if not node.successors:
        return node.score
    children = node.successors
    score = 0
    if level == 'min':
        while children:
            score = alpha_beta(children[0], node.inverse_level(), alpha, beta)
            if score < beta:
                beta = score
            if beta < alpha:
                return alpha
            children.pop(0)
        return beta
    else:
        while children:
            score = alpha_beta(children[0], node.inverse_level(), alpha, beta)
            if score > alpha:
                alpha = score
            if alpha > beta:
                return beta
            children.pop(0)
        return alpha
