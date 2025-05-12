# AI-Agent Implementation

## Agent Architecture Overview

```mermaid
graph TD
    A[User Input] --> B{Input Type}
    B -->|PDF| C[PDF Processing Agent]
    B -->|URL| D[Web Scraping Agent]
    C --> E[Text Extraction]
    D --> E
    E --> F[Gemini 1.5 Flash LLM Agent]
    F --> G[Summary Generation]
    G --> H[Output Display]

    style F fill:#ff9900,stroke:#333,stroke-width:4px
    style C fill:#87CEEB,stroke:#333,stroke-width:2px
    style D fill:#87CEEB,stroke:#333,stroke-width:2px
```

## Features

- Dual Input Processing:
  - PDF Document Analysis
  - Web Content Extraction
- Advanced LLM Integration with Gemini 1.5 Flash
- Real-time Processing
- Streamlit Interface

## Agent Components Architecture

### 1. Input Processing Agents
```mermaid
flowchart LR
    A[PDF Agent] -->|pdfplumber| B(Text Extraction)
    C[Web Agent] -->|BeautifulSoup| B
    B --> D{Content Processor}
```

### 2. LLM Agent Flow
```mermaid
sequenceDiagram
    participant U as User
    participant P as Processor
    participant G as Gemini Agent
    participant O as Output

    U->>P: Submit Content
    P->>G: Process Text
    G->>G: Apply Prompts
    G->>O: Generate Summary
    O->>U: Display Results
```

## Implementation Requirements

1. **Environment Setup**
```bash
pip install -r requirements.txt
```

2. **API Configuration**
```bash
# Create .env file
GOOGLE_API_KEY=your_api_key_here
```

3. **Application Launch**
```bash
streamlit run app.py
```

## Technical Architecture

### AI Agent Implementation Details

1. **PDF Processing Agent**
   - Core Component: pdfplumber
   - Functionality: Text extraction from multi-page documents
   - Error Handling: Format validation and extraction verification

2. **Web Scraping Agent**
   - Core Component: BeautifulSoup4
   - Functionality: Targeted content extraction
   - Error Handling: Connection management and timeout control

3. **Gemini LLM Agent**
   - Model: Gemini 1.5 Flash
   - Implementation: Chain-of-thought prompting
   - Processing: Zero-shot summarization
   - Integration: LangChain framework

```mermaid
graph TB
    subgraph "AI Agent Architecture"
    A[Input Layer] --> B[Processing Layer]
    B --> C[LLM Layer]
    C --> D[Output Layer]
    
    subgraph "Processing Layer"
    B1[PDF Agent]
    B2[Web Agent]
    end
    
    subgraph "LLM Layer"
    C1[Prompt Engineering]
    C2[Gemini 1.5 Flash]
    C3[Response Generation]
    end
    end
```


## Core Dependencies

- streamlit
- pdfplumber
- beautifulsoup4
- langchain
- google-generativeai
- python-dotenv
- requests

## Development

The source code implements three main agent components:
1. Document Processing Agent (PDF and Web)
2. Text Extraction and Processing Agent
3. LLM Integration Agent

For the complete implementation, refer to the `app.py` file in the repository.
