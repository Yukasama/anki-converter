export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <form
        method="post"
        action="/api/uploadfile"
        encType="multipart/form-data"
      >
        <input type="file" name="file" />
        <button type="submit">Convert</button>
      </form>
    </main>
  );
}
