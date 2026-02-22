def estimate_cost(input_tokens, output_tokens):
    INPUT_PRICE = 0.000005
    OUTPUT_PRICE = 0.000015

    return round(
        input_tokens * INPUT_PRICE +
        output_tokens * OUTPUT_PRICE,
        5,
    )