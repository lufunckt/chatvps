import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            # Builder URL
            url = "http://localhost:3123"
            print(f"Acessando {url}...")
            await page.goto(url, timeout=60000)
            await page.wait_for_timeout(5000) # Wait for JS to load
            await page.screenshot(path="screenshot_builder.png")
            print("Screenshot do Builder salvo como screenshot_builder.png")

            # Health Check
            await page.goto(f"{url}/api/health")
            print(await page.content())

        except Exception as e:
            print(f"Erro: {e}")
        finally:
            await browser.close()

asyncio.run(run())
