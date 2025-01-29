import os, sys, json

def main():
    # Paths
    input_fpath = '../data/expenses_2024.json'
    output_fpath = '../data/output/expenses_2024_transformed.json'

    # Load json
    data = {}
    with open(input_fpath, 'r') as f:
        data = json.load(f)
    print(f'data size: {len(data)}')
    
    # Transform data
    data_transformed = {}
    for k0, v0 in data.items():
        print(f'k0: {k0}')
        data_transformed[k0] = []

        for k1, v1 in v0.items():
            print(f'k1: {k1}')
            print(f'v1: {v1}')
            temp = {"type" : k1}
            temp.update(v1)
            print(f'temp: {temp}')
            data_transformed[k0].append(temp)

    # Save transformed data
    with open(output_fpath, 'w') as f:
        json.dump(data_transformed, f, indent=4)

if __name__ == '__main__':
    main()