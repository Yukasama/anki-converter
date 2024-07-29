'use client'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'

export default function Home() {
  return (
    <form method="POST" action="/api/uploadfile" encType="multipart/form-data">
      <div className="mx-6 my-10 flex flex-col items-center gap-5 md:m-20">
        <div className="flex flex-col items-center gap-1">
          <h2 className="text-4xl font-thin">Anki Converter</h2>
          <h4 className="text-sm text-neutral-400">
            Generate an Anki-PKG from a Markdown file
          </h4>
        </div>
        <Input type="file" name="file" accept=".md" className="w-96" />
        <Button>Generate</Button>
        <Separator className="md:my-5" />
        <div className="mt-2 flex w-full flex-col gap-3 rounded md:px-6 xl:w-[1200px]">
          <h2 className="text-lg font-semibold">
            How to format a Markdown file (.md)
          </h2>
          <div className="flex flex-col justify-between border xl:flex-row">
            <code className="flex-1 p-6 text-sm">
              <p>#### Welches Angebot bietet sich bei vertrauten Kunden an?</p>
              <p>Briefangebot (muss trotzdem &quot;wasserdicht&quot; sein)</p>
            </code>
            <div className="flex-1 bg-neutral-900 p-6">
              <p>Welches Angebot bietet sich bei vertrauten Kunden an?</p>
              <p>Briefangebot (muss trotzdem &quot;wasserdicht&quot; sein)</p>
            </div>
          </div>

          <div className="flex flex-col justify-between border xl:flex-row">
            <code className="flex-1 p-6 text-sm">
              <p>#### Wann ist ein Angebot ein umfangreiches Angebot?</p>
              <p>- 40-100 Seiten</p>
              <p>- Aufwendiges (Festpreis-)Projekt (mehrere Personenjahre)</p>
            </code>
            <div className="flex-1 bg-neutral-900 p-6">
              <p>Wann ist ein Angebot ein umfangreiches Angebot?</p>
              <p>- 40-100 Seiten</p>
              <p>- Aufwendiges (Festpreis-)Projekt (mehrere Personenjahre)</p>
            </div>
          </div>

          <div className="flex flex-col justify-between border xl:flex-row">
            <code className="flex-1 p-6 text-sm">
              <p>
                #### Wann ist ein Angebot ein umfangreiches Angebot? [Cloze]
              </p>
              <p>- 40-100 Seiten</p>
              <p>- Aufwendiges (Festpreis-)Projekt (mehrere Personenjahre)</p>
              <p className="mt-10 text-sm text-neutral-400">
                Here, two cards (one for each point) are being generated.
              </p>
            </code>
            <div className="flex-1 space-y-4 bg-neutral-900 p-6">
              <div>
                <p>Wann ist ein Angebot ein umfangreiches Angebot?</p>
                <p>{`{{c1:- 40-100 Seiten}}`}</p>
                <p>- Aufwendiges (Festpreis-)Projekt (mehrere Personenjahre)</p>
              </div>
              <div>
                <p>Wann ist ein Angebot ein umfangreiches Angebot?</p>
                <p>- 40-100 Seiten</p>
                <p>{`{{c2:- Aufwendiges (Festpreis-)Projekt (mehrere Personenjahre)}}`}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </form>
  )
}
