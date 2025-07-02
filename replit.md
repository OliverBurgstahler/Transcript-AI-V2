# YouTube Transcript Downloader

## Overview

This application is a YouTube Transcript Downloader that allows users to download transcripts from YouTube videos. It consists of a Flask backend API that fetches transcripts using the YouTube Transcript API with proxy support, and a web frontend that provides a user-friendly interface for inputting YouTube URLs and displaying extracted transcripts.

## System Architecture

The application follows a simple client-server architecture:

- **Frontend**: HTML/CSS/JavaScript web interface with Bootstrap styling and dark theme support
- **Backend**: Flask REST API with CORS enabled for cross-origin requests
- **External Service Integration**: YouTube Transcript API with proxy rotation for reliability
- **Proxy Management**: Built-in proxy rotation system using Webshare proxies

## Key Components

### Backend (app.py)
- **Flask Application**: Main web server handling API requests
- **Proxy Management**: Random proxy selection from a predefined list of Webshare proxies
- **Video ID Extraction**: Regex-based YouTube URL parsing to extract video IDs
- **Transcript Fetching**: Integration with YouTube Transcript API using proxy configuration
- **Error Handling**: Proxy testing and fallback mechanisms

### Frontend (youtube_transcript.html)
- **Dark Theme UI**: Bootstrap-based interface with dark theme support
- **Real-time Feedback**: Loading states, copy functionality, and URL validation
- **Responsive Design**: Mobile-friendly interface with proper viewport configuration
- **Interactive Elements**: Copy-to-clipboard functionality with visual feedback

### Legacy Frontend (index.html)
- **Simple Interface**: Basic HTML/CSS interface without Bootstrap
- **Download Functionality**: Direct text file download capability
- **Minimal Styling**: Clean, functional design with basic styling

## Data Flow

1. **User Input**: User enters YouTube URL in the web interface
2. **Frontend Validation**: JavaScript validates URL format and provides feedback
3. **API Request**: Frontend sends POST request to `/transcript` endpoint
4. **URL Processing**: Backend extracts video ID using regex patterns
5. **Proxy Selection**: Random proxy is selected from the available pool
6. **Transcript Fetching**: YouTube Transcript API is called with proxy configuration
7. **Response Processing**: Transcript data is formatted and returned to frontend
8. **Display**: Frontend renders the transcript with copy and download options

## External Dependencies

### Python Packages
- **Flask**: Web framework for the backend API
- **flask-cors**: Cross-Origin Resource Sharing support
- **youtube-transcript-api**: YouTube transcript extraction library
- **requests**: HTTP library for proxy testing

### Frontend Libraries
- **Bootstrap**: UI framework with dark theme support
- **Font Awesome**: Icon library for UI elements

### Third-party Services
- **Webshare Proxies**: Rotating proxy service for reliable YouTube API access
- **YouTube API**: Transcript data source (accessed via youtube-transcript-api)

## Deployment Strategy

The application is designed for simple deployment:

- **Development**: Local Flask development server on port 5000
- **CORS Configuration**: Enabled for cross-origin requests during development
- **Proxy Configuration**: Hardcoded proxy credentials (should be moved to environment variables for production)
- **Static Files**: HTML files served directly from the project root

### Production Considerations
- Move proxy credentials to environment variables
- Implement proper error logging
- Add rate limiting for API endpoints
- Consider containerization with Docker
- Implement proper secret management

## Changelog

- July 02, 2025: Initial setup with Flask backend and Bootstrap frontend
- July 02, 2025: Added centered transcript display and .txt download functionality
- July 02, 2025: Renamed application to "YouTube Transcript Downloader" throughout interface
- July 02, 2025: Added sidebar advertisement layout with 4 ad spaces (2 left, 2 right)

## User Preferences

Preferred communication style: Simple, everyday language.