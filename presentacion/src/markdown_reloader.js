export default function MarkdownReloader() {
  return {
    name: 'markdown-reloader',
    enforce: 'post',
    
    handleHotUpdate({ file, server }) {
      if (file.endsWith('.md')) {
        console.log('reloading markdown...');

        server.ws.send({
          type: 'full-reload',
          path: '*'
        });
      }
    },
  }
}
