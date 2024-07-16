export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <form
        method="POST"
        action="/api/uploadfile"
        encType="multipart/form-data"
      >
        <input type="file" name="file" />
        <button type="submit">Let's go</button>
      </form>
    </main>
  );
}