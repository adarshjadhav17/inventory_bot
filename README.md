\documentclass{article}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
}
\usepackage{listings}
\usepackage{xcolor}

\definecolor{codebg}{rgb}{0.95,0.95,0.95}
\lstset{
    backgroundcolor=\color{codebg},
    basicstyle=\ttfamily,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{red},
    frame=single,
    breaklines=true,
    postbreak=\mbox{\textcolor{red}{$\hookrightarrow$}\space},
    numbers=left,
    numberstyle=\tiny,
    numbersep=5pt,
    language=Python
}

\begin{document}

\title{T-Shirt Inventory Dashboard}
\author{}
\date{}
\maketitle

\section*{Overview}
The T-Shirt Inventory Dashboard is a web-based application built using Python, OpenSearch, and Streamlit. It allows users to search for inventory items and calculate the total inventory price for specific sizes in a t-shirt inventory database.

\section*{Features}
\begin{itemize}
    \item Search for t-shirt inventory by brand and size.
    \item Calculate the total inventory price for t-shirts of a specific size.
    \item Uses OpenSearch for indexing and querying inventory data.
    \item Built with Streamlit for a user-friendly dashboard interface.
\end{itemize}

\section*{Technologies Used}
\begin{itemize}
    \item \textbf{Python}: Backend scripting.
    \item \textbf{OpenSearch}: Indexing and querying inventory data.
    \item \textbf{Streamlit}: Frontend dashboard development.
    \item \textbf{dotenv}: For managing environment variables.
    \item \textbf{JSON}: For storing and loading inventory data.
\end{itemize}

\section*{Setup and Installation}
\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}
    git clone https://github.com/your-username/tshirt-inventory-dashboard.git
    \end{lstlisting}
    \item Install dependencies:
    \begin{lstlisting}
    pip install -r requirements.txt
    \end{lstlisting}
    \item Create a \texttt{.env} file and add your OpenSearch credentials:
    \begin{lstlisting}
    OPENSEARCH_URL="https://your-opensearch-endpoint"
    OPENSEARCH_USERNAME="your-username"
    OPENSEARCH_PASSWORD="your-password"
    \end{lstlisting}
    \item Run the Streamlit app:
    \begin{lstlisting}
    streamlit run app.py
    \end{lstlisting}
\end{enumerate}

\section*{How to Use}
\subsection*{1. Search Inventory}
\begin{itemize}
    \item Enter the brand name in the text input field.
    \item Select the desired t-shirt size from the dropdown menu.
    \item Click the \textbf{Search} button to view matching inventory items.
\end{itemize}

\subsection*{2. Calculate Inventory Price}
\begin{itemize}
    \item Select the desired t-shirt size from the dropdown menu.
    \item Click the \textbf{Calculate} button to view the total inventory price for the selected size.
\end{itemize}

\section*{Code Explanation}
\begin{itemize}
    \item \textbf{create\_index}: Creates the OpenSearch index with predefined settings and mappings.
    \item \textbf{load\_data}: Loads inventory data from a JSON file into the OpenSearch index.
    \item \textbf{search\_data}: Searches the inventory for specific criteria using OpenSearch queries.
    \item \textbf{get\_total\_inventory\_price}: Calculates the total inventory price for a specific size using OpenSearch aggregations.
    \item \textbf{Streamlit Dashboard}: Provides an interactive interface for users to query and analyze inventory data.
\end{itemize}

\section*{Data Format}
The JSON data for loading inventory should be structured as follows:
\begin{lstlisting}[language=json]
[
    {
        "brand": "BrandA",
        "size": "M",
        "price": 20.0,
        "stock_quantity": 100
    },
    {
        "brand": "BrandB",
        "size": "L",
        "price": 25.0,
        "stock_quantity": 50
    }
]
\end{lstlisting}

\section*{Acknowledgements}
This project uses:
\begin{itemize}
    \item \href{https://opensearch.org/}{OpenSearch} for indexing and searching data.
    \item \href{https://streamlit.io/}{Streamlit} for building the dashboard interface.
    \item \href{https://pypi.org/project/python-dotenv/}{dotenv} for environment variable management.
\end{itemize}

\section*{License}
This project is licensed under the MIT License. See the \texttt{LICENSE} file for details.

\end{document}
