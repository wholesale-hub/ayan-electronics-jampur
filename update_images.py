from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Update product image URLs inside PRODUCTS_DB
start = text.index('const PRODUCTS_DB = [')
end = text.index('];', start) + 2
products = text[start:end]
lines = products.splitlines()
sig = 1
new_lines = []
for line in lines:
    if re.match(r'\s*img:\s*"', line):
        prefix = line[:line.index('img:')]
        new_url = 'https://source.unsplash.com/featured/500x500/?electronics-parts&sig=' + str(sig)
        line = f'{prefix}img: "{new_url}",' 
        sig += 1
    new_lines.append(line)
new_products = '\n'.join(new_lines)
text = text[:start] + new_products + text[end:]

# Replace team section block with provided profile images only
team_start = text.index('<!-- Auto-scrolling team carousel')
team_end = text.index('</section>', team_start) + len('</section>')
new_team = '''<!-- Auto-scrolling team carousel -->
      <div class="team-slider-outer">
        <div class="team-slider-track" id="teamSliderTrack">

          <div class="team-card-premium">
            <img src="yameen.png" alt="Muhammad Yameen Leshari" class="team-card-avatar">
            <h3 class="team-card-name">Muhammad Yameen Leshari</h3>
            <div class="team-card-role">Owner & Chief Handler</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

          <div class="team-card-premium">
            <img src="Muhammad%20Rizwan.png" alt="Muhammad Rizwan" class="team-card-avatar">
            <h3 class="team-card-name">Muhammad Rizwan</h3>
            <div class="team-card-role">Wholesale Manager</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

          <div class="team-card-premium">
            <img src="naveed.png" alt="Naveed" class="team-card-avatar">
            <h3 class="team-card-name">Naveed</h3>
            <div class="team-card-role">Senior Inverter Expert</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

          <div class="team-card-premium">
            <img src="Younis.png" alt="Younis" class="team-card-avatar">
            <h3 class="team-card-name">Younis</h3>
            <div class="team-card-role">UPS Repairing Specialist</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

          <div class="team-card-premium">
            <img src="zain.png" alt="Zain" class="team-card-avatar">
            <h3 class="team-card-name">Zain</h3>
            <div class="team-card-role">Solar Systems Installer</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

          <div class="team-card-premium">
            <img src="Zeeshan.png" alt="Zeeshan" class="team-card-avatar">
            <h3 class="team-card-name">Zeeshan</h3>
            <div class="team-card-role">Battery Diagnostics Engineer</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

          <div class="team-card-premium">
            <img src="Kounain.png" alt="Kounain" class="team-card-avatar">
            <h3 class="team-card-name">Kounain</h3>
            <div class="team-card-role">Hardware Quality Manager</div>
            <a href="tel:03333301123" class="team-card-phone"><i class="fa-solid fa-phone"></i> 03333301123</a>
          </div>

        </div>
      </div>
    </section>'''
text = text[:team_start] + new_team + text[team_end:]

# Update team animation for full scroll loop
text = text.replace('  0%   { transform: translateX(0); }\n      100% { transform: translateX(-50%); }', '  0%   { transform: translateX(0); }\n      100% { transform: translateX(-100%); }')

path.write_text(text, encoding='utf-8')
print('updated')
