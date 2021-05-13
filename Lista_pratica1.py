{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Lista_pratica1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNfQExmaRS1euJMrtrp3PV4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yingyangtongxue/Numerical_Calculus/blob/main/Lista_pratica1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W6e0TdpyqfIe"
      },
      "source": [
        "import numpy as np\n",
        "\n",
        "def is_Symmetrical(M):\n",
        "    for i in range(len(M)):\n",
        "        for j  in range(len(M[0])):\n",
        "            if M[i][j] != M[j][i]:\n",
        "                return False\n",
        "    return True\n",
        "\n",
        "def square(M):\n",
        "    M = np.array(M)\n",
        "    if M.shape[0] == M.shape[1]:\n",
        "      return True\n",
        "    return False\n",
        "\n",
        "def isMatrixPositive(M):\n",
        "  n = np.shape(M)[0] #first row length\n",
        "  for i in range(n):\n",
        "    if not M[i][i] > 0:\n",
        "      return False\n",
        "  return True"
      ],
      "execution_count": 67,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jovqD2PUZWoo"
      },
      "source": [
        "# **Decomposição LU**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WfWvkFY7YH9p"
      },
      "source": [
        "import numpy as np\n",
        "\n",
        "def LU_decomposition(A):\n",
        "  A = np.array(A,dtype=float) #convert to float list\n",
        "  U = np.copy(A) \n",
        "  n = np.shape(U)[0] #first row length\n",
        "  L = np.eye(n) #Identity matrix\n",
        "  for j in np.arange(n-1): # j = row (start -> j=0 in [0,1,...,n-1])\n",
        "    for i in np.arange(j+1,n): # i = column (start -> i=0 in [j+1,j+2,...,n])\n",
        "      L[i,j] = U[i,j]/U[j,j] \n",
        "      for k in np.arange(j+1,n):\n",
        "        old = U[i,k]\n",
        "        U[i,k] = U[i,k] - L[i,j] * U[j,k]\n",
        "      U[i,j] = 0\n",
        "\n",
        "  return L,U"
      ],
      "execution_count": 68,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aDH9Ftr8aJJN"
      },
      "source": [
        "1) Escreva uma função em Python para realizar a decomposição LU, e depois teste\n",
        "seu algoritmo para as seguintes matrizes:\n",
        "\n",
        "a) A = [[2.0,-1.0,1.0],\n",
        "     [3.0,3.0,9.0],\n",
        "     [3.0,3.0,5.0]]\n",
        "\n",
        "b) A = [[1.012,-2.132,3.104],\n",
        "      [-2.132,4.906,-7.013],\n",
        "      [3.104,-7.013,0.014]]\n",
        "\n",
        "c) A = [[2,0,0,0],\n",
        "      [1,1.5,0,0],\n",
        "      [0,-3,0.5,0],\n",
        "      [2,-2,1,1]]\n",
        "\n",
        "d) A = [[2.1756,4.0231,-2.1732,5.1967],\n",
        "        [-4.0231,6.0000,0,1.1973],\n",
        "        [-1.0000,-5.2107,1.1111,0],\n",
        "        [6.0235,7.0000,0,-4.1561]]\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "njfyb-5YbFeV"
      },
      "source": [
        "RESOLUÇÃO:\n",
        "\n",
        "1-a)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gu5b0XhEakCf",
        "outputId": "746cc893-c0ab-4272-875d-30f61a5b1add"
      },
      "source": [
        "A = [[2.0,-1.0,1.0],\n",
        "     [3.0,3.0,9.0],\n",
        "     [3.0,3.0,5.0]]\n",
        "\n",
        "print(\"\\nRESULTADO 1-A: \\n\")\n",
        "\n",
        "L, U = LU_decomposition(A)\n",
        "\n",
        "print(\"\\n A = L * U\")\n",
        "print(\"\\nA:\\n\",A)\n",
        "print(\"\\nL (Lower Matrix):\\n\",L)\n",
        "print(\"\\nU (Upper Matrix):\\n\",U)"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 1-A: \n",
            "\n",
            "\n",
            " A = L * U\n",
            "\n",
            "A:\n",
            " [[2.0, -1.0, 1.0], [3.0, 3.0, 9.0], [3.0, 3.0, 5.0]]\n",
            "\n",
            "L (Lower Matrix):\n",
            " [[1.  0.  0. ]\n",
            " [1.5 1.  0. ]\n",
            " [1.5 1.  1. ]]\n",
            "\n",
            "U (Upper Matrix):\n",
            " [[ 2.  -1.   1. ]\n",
            " [ 0.   4.5  7.5]\n",
            " [ 0.   0.  -4. ]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-tHQwFBMczOb"
      },
      "source": [
        "1-b)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XyuFOcMpcf5f",
        "outputId": "3e60e8da-42c1-4f28-cdc8-64667575bd03"
      },
      "source": [
        "A = [[1.012,-2.132,3.104],\n",
        "    [-2.132,4.906,-7.013],\n",
        "    [3.104,-7.013,0.014]]\n",
        "\n",
        "print(\"\\nRESULTADO 1-B: \\n\")\n",
        "\n",
        "L, U = LU_decomposition(A)\n",
        "\n",
        "print(\"\\n A = L * U\")\n",
        "print(\"\\nA:\\n\",A)\n",
        "print(\"\\nL (Lower Matrix):\\n\",L)\n",
        "print(\"\\nU (Upper Matrix):\\n\",U)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 1-B: \n",
            "\n",
            "\n",
            " A = L * U\n",
            "\n",
            "A:\n",
            " [[1.012, -2.132, 3.104], [-2.132, 4.906, -7.013], [3.104, -7.013, 0.014]]\n",
            "\n",
            "L (Lower Matrix):\n",
            " [[ 1.          0.          0.        ]\n",
            " [-2.10671937  1.          0.        ]\n",
            " [ 3.06719368 -1.14299746  1.        ]]\n",
            "\n",
            "U (Upper Matrix):\n",
            " [[  1.012       -2.132        3.104     ]\n",
            " [  0.           0.41447431  -0.47374308]\n",
            " [  0.           0.         -10.04805631]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gj2Yr0Q8eS-M"
      },
      "source": [
        "1-c)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U_JtvF7Ldyrf",
        "outputId": "34c829c9-c248-438c-f6b5-275e993c1a28"
      },
      "source": [
        "A = [[2,0,0,0],\n",
        "      [1,1.5,0,0],\n",
        "      [0,-3,0.5,0],\n",
        "      [2,-2,1,1]]\n",
        "     \n",
        "print(\"\\nRESULTADO 1-C: \\n\")\n",
        "\n",
        "L, U = LU_decomposition(A)\n",
        "\n",
        "print(\"\\n A = L * U\")\n",
        "print(\"\\nA:\\n\",A)\n",
        "print(\"\\nL (Lower Matrix):\\n\",L)\n",
        "print(\"\\nU (Upper Matrix):\\n\",U)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 1-C: \n",
            "\n",
            "\n",
            " A = L * U\n",
            "\n",
            "A:\n",
            " [[2, 0, 0, 0], [1, 1.5, 0, 0], [0, -3, 0.5, 0], [2, -2, 1, 1]]\n",
            "\n",
            "L (Lower Matrix):\n",
            " [[ 1.          0.          0.          0.        ]\n",
            " [ 0.5         1.          0.          0.        ]\n",
            " [ 0.         -2.          1.          0.        ]\n",
            " [ 1.         -1.33333333  2.          1.        ]]\n",
            "\n",
            "U (Upper Matrix):\n",
            " [[2.  0.  0.  0. ]\n",
            " [0.  1.5 0.  0. ]\n",
            " [0.  0.  0.5 0. ]\n",
            " [0.  0.  0.  1. ]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gPWzzdq6eYqd"
      },
      "source": [
        "1-d)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LljUlM3qeXnq",
        "outputId": "816b4a2e-482c-4d65-f6ac-fa15e68e358b"
      },
      "source": [
        "A = [[2.1756,4.0231,-2.1732,5.1967],\n",
        "        [-4.0231,6.0000,0,1.1973],\n",
        "        [-1.0000,-5.2107,1.1111,0],\n",
        "        [6.0235,7.0000,0,-4.1561]]\n",
        "\n",
        "print(\"\\nRESULTADO 1-D: \\n\")\n",
        "\n",
        "L, U = LU_decomposition(A)\n",
        "\n",
        "print(\"\\n A = L * U\")\n",
        "print(\"\\nA:\\n\",A)\n",
        "print(\"\\nL (Lower Matrix):\\n\",L)\n",
        "print(\"\\nU (Upper Matrix):\\n\",U)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 1-D: \n",
            "\n",
            "\n",
            " A = L * U\n",
            "\n",
            "A:\n",
            " [[2.1756, 4.0231, -2.1732, 5.1967], [-4.0231, 6.0, 0, 1.1973], [-1.0, -5.2107, 1.1111, 0], [6.0235, 7.0, 0, -4.1561]]\n",
            "\n",
            "L (Lower Matrix):\n",
            " [[ 1.          0.          0.          0.        ]\n",
            " [-1.84919103  1.          0.          0.        ]\n",
            " [-0.45964332 -0.25012194  1.          0.        ]\n",
            " [ 2.76866152 -0.30794361 -5.35228302  1.        ]]\n",
            "\n",
            "U (Upper Matrix):\n",
            " [[ 2.1756      4.0231     -2.1732      5.1967    ]\n",
            " [ 0.         13.43948042 -4.01866194 10.80699101]\n",
            " [ 0.          0.         -0.89295239  5.09169403]\n",
            " [ 0.          0.          0.         12.03612803]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "riliqkYDpDiy"
      },
      "source": [
        "# **Decomposição Cholesky**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Bp4MZIeHpPUu"
      },
      "source": [
        "2) Escreva uma função em Python para realizar a decomposição Cholesky, e\n",
        "depois teste seu algoritmo para as seguintes matrizes:\n",
        "\n",
        "a) A = [[2,-1,0],\n",
        "      [-1,2,-1],\n",
        "      [0,-1,2]]\n",
        "\n",
        "b) A = [[4,1,1,1],\n",
        "      [1,3,-1,1],\n",
        "      [1,-1,2,0],\n",
        "      [1,1,0,2]]\n",
        "\n",
        "c) A = [[4,1,-1,0],\n",
        "      [1,3,-1,0],\n",
        "      [-1,-1,5,2],\n",
        "      [0,0,2,4]]\n",
        "\n",
        "d) A = [[6,2,1,-1],\n",
        "      [2,4,1,0],\n",
        "      [1,1,4,-1],\n",
        "      [-1,0,-1,3]]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ukqpm3UzVSu8"
      },
      "source": [
        "def cholesky_Decomposition(A):\n",
        "  A = np.array(A,dtype=float) #convert to float list\n",
        "  if not square(A):\n",
        "    print(\"Error! The matrix isn't square\")\n",
        "  if not (isMatrixPositive(A) and is_Symmetrical(A)): # elements above and below the main diagonal must be equal \n",
        "    print(\"Error! The matrix isn't symmetric\")\n",
        "  else:\n",
        "    n = A.shape[0]\n",
        "    L = np.zeros_like(A)\n",
        "    for i in range(n):\n",
        "        L[i,i] = np.sqrt(A[i,i])\n",
        "        L[i+1:,i] = A[i+1:,i] / L[i, i]\n",
        "        for j in range(i+1,n):\n",
        "            A[j:,j] = A[j:,j] - L[j,i] * L[j:,i]\n",
        "    return L         "
      ],
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ceXDMXVuiPp7"
      },
      "source": [
        "2-a)\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jWW6t2WsiUJh",
        "outputId": "892defea-08a6-43d4-e615-e9b51ec0bdf2"
      },
      "source": [
        "A = [[2,-1,0],\n",
        "      [-1,2,-1],\n",
        "      [0,-1,2]]\n",
        "\n",
        "print(\"\\nRESULTADO 2-A: \\n\")\n",
        "cholesky_Decomposition(A)  "
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 2-A: \n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 1.41421356,  0.        ,  0.        ],\n",
              "       [-0.70710678,  1.22474487,  0.        ],\n",
              "       [ 0.        , -0.81649658,  1.15470054]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G4uKNIVgiUlp"
      },
      "source": [
        "2-b)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jmv9EP8hiWno",
        "outputId": "76f54fbc-62ae-49cd-d49f-20debd5c4d3e"
      },
      "source": [
        "A = [[4,1,1,1],\n",
        "      [1,3,-1,1],\n",
        "      [1,-1,2,0],\n",
        "      [1,1,0,2]]\n",
        "\n",
        "print(\"\\nRESULTADO 2-B: \\n\")\n",
        "cholesky_Decomposition(A)  "
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 2-B: \n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 2.        ,  0.        ,  0.        ,  0.        ],\n",
              "       [ 0.5       ,  1.6583124 ,  0.        ,  0.        ],\n",
              "       [ 0.5       , -0.75377836,  1.08711461,  0.        ],\n",
              "       [ 0.5       ,  0.45226702,  0.0836242 ,  1.24034735]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MIgYqRkjiY4q"
      },
      "source": [
        "2-c)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GM8nHIo6ihus",
        "outputId": "14f3ee44-0989-49ab-f74b-d44a2e678c1a"
      },
      "source": [
        "A = [[4,1,-1,0],\n",
        "      [1,3,-1,0],\n",
        "      [-1,-1,5,2],\n",
        "      [0,0,2,4]]\n",
        "\n",
        "print(\"\\nRESULTADO 2-C: \\n\")\n",
        "cholesky_Decomposition(A)  "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 2-C: \n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 2.        ,  0.        ,  0.        ,  0.        ],\n",
              "       [ 0.5       ,  1.6583124 ,  0.        ,  0.        ],\n",
              "       [-0.5       , -0.45226702,  2.13200716,  0.        ],\n",
              "       [ 0.        ,  0.        ,  0.93808315,  1.76635217]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 79
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PhYDlk-Vib1i"
      },
      "source": [
        "2-d)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AZspe2aMiitC",
        "outputId": "44dae1b0-21b0-4a6c-c1bd-1371eb81b160"
      },
      "source": [
        "A = [[6,2,1,-1],\n",
        "      [2,4,1,0],\n",
        "      [1,1,4,-1],\n",
        "      [-1,0,-1,3]]\n",
        "\n",
        "print(\"\\nRESULTADO 2-D: \\n\")\n",
        "cholesky_Decomposition(A)  "
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "RESULTADO 2-D: \n",
            "\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 2.44948974,  0.        ,  0.        ,  0.        ],\n",
              "       [ 0.81649658,  1.82574186,  0.        ,  0.        ],\n",
              "       [ 0.40824829,  0.36514837,  1.92353841,  0.        ],\n",
              "       [-0.40824829,  0.18257419, -0.46788772,  1.60657433]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    }
  ]
}