# AI Resume Analyzer

An intelligent resume analysis tool powered by LLMs (Large Language Models) and Streamlit. This application analyzes resumes, extracts skills, provides improvement suggestions, and matches resumes against job descriptions.

## Features

- **Complete Resume Analysis**: Comprehensive analysis including summary, skills, experience level, strengths, and improvements
- **Skill Extraction**: Automatically categorize technical skills, soft skills, tools, and languages
- **Improvement Suggestions**: Get specific recommendations to enhance your resume
- **Job Match Analysis**: Match your resume against job descriptions with match scores
- **Multi-Format Support**: Upload PDF, DOCX, or TXT files
- **Multiple LLM Providers**: Support for OpenAI, Anthropic, and Hugging Face
- **Customizable Analysis**: Adjust temperature and model selection for different analysis styles

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

5. Add your API keys to `.env`:
```
OPENAI_API_KEY=your_api_key_here
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Analyzer

1. **Upload Resume**: Click the upload area and select your resume file (PDF, DOCX, or TXT)
2. **Configure Settings**: 
   - Select LLM provider (OpenAI, Anthropic, Hugging Face)
   - Choose the model
   - Adjust temperature for creativity level
3. **Select Analysis Type**:
   - Complete Analysis
   - Skill Extraction
   - Improvement Suggestions
   - Job Match Analysis (requires job description)
4. **View Results**: Results are displayed in the results panel
5. **Download**: Export results as JSON/TXT

## Project Structure

```
ai-resume-analyzer/
├── app.py                      # Main Streamlit application
├── src/
│   ├── __init__.py
│   ├── resume_analyzer.py      # Core analyzer logic
│   └── utils.py                # Utility functions
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .gitignore
└── README.md                   # This file
```

## API Configuration

### OpenAI Setup
1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Add to `.env`:
```
OPENAI_API_KEY=sk-...
```

### Anthropic Setup
1. Get your API key from [Anthropic Console](https://console.anthropic.com/)
2. Add to `.env`:
```
ANTHROPIC_API_KEY=sk-ant-...
```

## Features in Detail

### Complete Analysis
Provides comprehensive analysis including:
- Candidate summary
- Identified skills (categorized)
- Experience level assessment
- Key strengths
- Areas for improvement
- Recommended enhancements

### Skill Extraction
Categorizes skills into:
- Technical skills
- Soft skills
- Tools and technologies
- Programming languages
- Other relevant skills

### Improvement Suggestions
Offers actionable recommendations for:
- Formatting improvements
- Content enhancements
- Missing sections
- Common skill gaps
- Prioritized action items

### Job Match Analysis
Analyzes resume-to-job fit:
- Match score (0-100)
- Matching skills
- Missing skills
- Relevant experience matches
- Specific recommendations
- Confidence level

## Supported File Formats

- **PDF** (.pdf)
- **Word Documents** (.docx)
- **Text Files** (.txt)

## Requirements

- Python 3.8+
- Streamlit 1.0+
- OpenAI API key (for OpenAI models)
- Anthropic API key (for Claude models)
- Python libraries: see requirements.txt

## Troubleshooting

### API Key Errors
- Ensure `.env` file exists in the project root
- Check API keys are correctly formatted
- Verify API key permissions and limits

### PDF Extraction Issues
- Ensure PDF is not password protected
- Try converting PDF to another format
- Check PyPDF2 version compatibility

### Streamlit Issues
- Clear cache: `streamlit cache clear`
- Update Streamlit: `pip install --upgrade streamlit`

## Performance Tips

- Use GPT-3.5-turbo for faster analysis
- Lower temperature for more consistent results
- Batch multiple resumes for analysis

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for informational purposes. Results should be reviewed by humans before making career decisions.

## Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the maintainers.

## Roadmap

- [ ] Resume scoring and ranking
- [ ] Batch resume processing
- [ ] Resume template suggestions
- [ ] Export to multiple formats
- [ ] Integration with job boards
- [ ] Cover letter generation
- [ ] Interview preparation suggestions

---

Made with ❤️ using Streamlit and AI
