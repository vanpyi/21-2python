{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPBdkFq+XhU92Jro3Jfd5r6",
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
        "<a href=\"https://colab.research.google.com/github/vanpyi/21-2python/blob/main/210906.%EC%8B%A4%EC%8A%B5%EC%BD%94%EB%93%9C1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3-DltWNWcKfy",
        "outputId": "f79af479-0b8f-49ba-8916-3bdc25b39bfc"
      },
      "source": [
        "#2. 두 정수 A와 B를 입력받은 다음.\n",
        "# A+B를 출력하는 프로그램을 작성하시오\n",
        "a, b = input().split()\n",
        "a = int(a)\n",
        "b = int(b)\n",
        "print(a+b)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G42ucn5pc9qC",
        "outputId": "fe37297c-24f3-4d37-c313-76692fb28fc3"
      },
      "source": [
        "# 두 자연수 A와 B가 주어진다.\n",
        "# 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. \n",
        "A, B = input().split()\n",
        "A = int(A)\n",
        "B = int(B)\n",
        "print(A+B)\n",
        "print(A-B)\n",
        "print(A*B)\n",
        "print(A//B)\n",
        "print(A%B)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7 3\n",
            "10\n",
            "4\n",
            "21\n",
            "2\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XFHd2OfBgr7h",
        "outputId": "bc75e7a8-8b61-4c13-8537-3abf4dd09e57"
      },
      "source": [
        "# 시험 점수를 입력받아 \n",
        "# 90 ~ 100점은 A, 80 ~ 89점은 B,\n",
        "# 70 ~ 79점은 C, \n",
        "# 60 ~ 69점은 D, \n",
        "# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.\n",
        "\n",
        "score = int(input())\n",
        "if score>=90 :\n",
        "  print(\"A\")\n",
        "elif score>=80 :\n",
        "  print(\"B\")\n",
        "elif score>=70 :\n",
        "  print(\"C\")\n",
        "elif score>=60 :\n",
        "  print(\"D\")\n",
        "else:\n",
        "  print(\"F\")"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n",
            "A\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f2IbIMUGnygs"
      },
      "source": [
        "# 두 정수 A와 B가 주어졌을 때,\n",
        "# A와 B를 비교하는 프로그램을 작성하시오.\n",
        "\n",
        "A, B = int()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}