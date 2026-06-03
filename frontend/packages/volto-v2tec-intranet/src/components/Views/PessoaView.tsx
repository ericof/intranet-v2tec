import React from 'react';
import Image from '@plone/volto/components/theme/Image/Image';
import { Container } from '@plone/components';
import ContactInfo from 'volto-v2tec-intranet/components/ContactInfo/ContactInfo';
import EnderecoInfo from 'volto-v2tec-intranet/components/EnderecoInfo/EnderecoInfo';
import type { Pessoa } from 'volto-v2tec-intranet/types/content';

interface PessoaViewProps {
  content: Pessoa;
  [key: string]: any;
}

const PessoaView: React.FC<PessoaViewProps> = (props) => {
  const { content } = props;

  return (
    <Container id="page-document" className="view-wrapper pessoa-view">
      {content.image && (
        <Image
          className="documentImage ui right floated image"
          alt={content.title}
          title={content.title}
          item={content}
          imageField="image"
          responsive={true}
        />
      )}
      <h1 className="documentFirstHeading">{content.title}</h1>
      {content.description && (
        <p className="documentDescription">{content.description}</p>
      )}
      <ContactInfo content={content} />
      <EnderecoInfo content={content} />
    </Container>
  );
};

export default PessoaView;
