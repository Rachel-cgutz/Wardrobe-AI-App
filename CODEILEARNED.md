with statements: with statements enter context of how a file or layout should act/look.
the with statement tells python to play by the rules of the object in question through
the indented lines beneath it. Once the code exits the block it exits the context/rules of the object.
"What stays in the with statement, stays in the with statement" (only context stays)

vector databases: vector databases are a place to store data/embeddings and quickly retrieve data semantically through vector embeddings. A process of vector indexing which uses ANN algorithms to find closest matches to the query vector. A vector database is also a part of RAG where the vector database stores knowledge and embeddings, this allows LLMs to answer questions without having the exact answer by providing context and similar embeddings from the vector database.

try, except, finally: The try block contains code that might cause an error, and if
an error occurs the except block will execute which lays out how to handle the error. The finally block runs whether or not an error occurred or not. For example: try block will run 'connect to database' - if there is an error the except block will print 'Check your database connection.' - then the finally block will disconnect from database whether or not it successfully connected.

positional argument: if in a positional argument a raw value can get passed without using parameter names but may crash if collaborating with others who use keyword arguments and the parameters were renamed, you can use a / to restrict to only use positional arguments so the code does not crash if parameters are renamed. A positional argument always comes before a keyword argument, and a positional argument follows a sequence order from 1st..2nd..so on

https://youtu.be/T-D1OfcDW1M - What is RAG?
Retrieval-Augmented Generation frameworks help to solve 2 challenges LLMs face: No supportive evidence (hallucinating answers) and being out of date. RAG creates a content store from which the model can refer to first before answering providing evidence from relevant sources. This also helps when updating data, only the content store needs to get updated and the model does not need to get trained again.

https://youtu.be/e9U0QAFbfLI - Cosine Similarity.
Cosine Similarity is a way to measure how similar two phrases or images are by calculating the angle between them (once they have been vectorized). Cosine = 1 means they are the exact same, Cosine = 0 (orthogonal) completely independent, Cosine = -1 opposites.

https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval - Multimodal Embeddings.
Keyword search retrieves images with the same words in a users query as found in an image label/description, Vector search measures the cosine similarity between the text and the image (search semantically by breaking down meaning and context of the query).
*Vector embeddings can only be matched by the same model*. Image retrieval process: input text and images get vectorized and return a single feature vector(embedding), cosine similarity or any distance metric (euclidean) is measured, the top image embedding most similar to the query text is shown.

https://fyntuneq.com/blog/semantic-similarity-vs-exact-match-in-llm-testing - Exact match vs. Semantic match.
Exact match is better for inputs and outputs to follow specific form and structure- it cannot detect synonyms. Semantic matching is better to preserve meaning - it can detect synonyms but may not detect near-antonyms, cosine similarity can be warped if the domain is unfamiliar and the text is too short.
