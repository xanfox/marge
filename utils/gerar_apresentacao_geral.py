def gerar_apresentacao_geral(nome_completo: str, pronomes: dict) -> str:
    primeiro_nome = nome_completo.split()[0]

    return f"""
<p><strong>{pronomes['pronome_bemvindo']}, {nome_completo}.</strong></p>

<p>Este é o seu <strong>Círculo Interior</strong> — uma jornada de autoconhecimento construída especialmente para você, {primeiro_nome}. Cada elemento deste mapa revela facetas importantes da sua essência, suas forças, desafios, caminhos e potenciais ocultos.</p>

<p>Não se trata de previsões absolutas, mas de espelhos simbólicos para reflexão. O objetivo é te ajudar a enxergar padrões, validar sentimentos e, principalmente, reconectar você com o seu próprio eixo.</p>

<p><strong>O que você vai encontrar aqui são 7 ferramentas:</strong></p>
<ul>
  <li>☀️ <strong>Signo Solar</strong> — traços centrais da sua personalidade</li>
  <li>🌙 <strong>Signo Lunar</strong> — como você sente e reage emocionalmente</li>
  <li>↗️ <strong>Ascendente</strong> — a forma como o mundo te enxerga</li>
  <li>🔢 <strong>Caminho de Vida</strong> — sua trajetória numerológica</li>
  <li>🎴 <strong>Arcano Regente</strong> — seu arquétipo espiritual no Tarot</li>
  <li>🌳 <strong>Signo Celta</strong> — sua árvore sagrada e simbologia ancestral</li>
  <li>🐉 <strong>Signo Chinês</strong> — seu arquétipo no zodíaco oriental</li>
</ul>

<p>Use este material com calma. Leia um tópico por vez, anote insights, volte sempre que sentir necessidade. O autoconhecimento não é uma linha reta — é um processo vivo, que se renova cada vez que olhamos para dentro com mais presença e curiosidade.</p>

<p>Gratidão por permitir que essa leitura chegue até você, {primeiro_nome}. Que {pronomes['pronome_sujeito']} encontre reflexos verdadeiros {pronomes['pronome_objeto']} e siga sua caminhada com mais consciência.</p>

<p><em>🔮 Criado por Alex, seu consultor de tarot | <a href="https://7caballa.com.br" target="_blank">7caballa.com.br</a> | <a href="https://wa.me/SEUNUMEROAQUI" target="_blank">Fale comigo no WhatsApp</a></em></p>
"""
