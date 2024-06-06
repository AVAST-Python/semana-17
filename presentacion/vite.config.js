import { defineConfig } from 'vite' // For autocompletion in VSCode
import { resolve } from 'path'
import MarkdownReloader from './src/markdown_reloader'
import copy from 'rollup-plugin-copy'

const root = resolve(__dirname, 'src')
const outDir = resolve(__dirname, 'dist')

export default defineConfig({
  // config options
  root,
  base: "./",
  plugins: [
    // We need to copy the chalkboard images to the dist folder because are referenced from an external script
    copy({
      targets: [{ src: 'src/plugin/chalkboard/img', dest: 'dist/plugin/chalkboard' }],
      hook: 'writeBundle' // notice here
    }),
    MarkdownReloader() // Reloads on markdown changes
  ],
  build: {
    outDir,
    emptyOutDir: true,
    chunkSizeWarningLimit: 1200, //Kb
    rollupOptions: {
      input: {
        main: resolve(root, 'index.html'),
        // You can add more entrypoints here
      }
    }
  }
})
